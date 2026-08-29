#!/usr/bin/env python3
"""Update lifetime downloads and recently updated releases in the root README."""

from __future__ import annotations

import html
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
GAMES_PATH = ROOT / "games"
START_MARKER = "<!-- top-downloads:start -->"
END_MARKER = "<!-- top-downloads:end -->"
RECENT_START_MARKER = "<!-- recent-updates:start -->"
RECENT_END_MARKER = "<!-- recent-updates:end -->"
DEFAULT_REPOSITORY = "Linbin-Lai/5050-hanhua"
TOP_N = 10


def github_get(url: str, token: str | None) -> tuple[object, dict[str, str]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "5050-hanhua-top-downloads",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=30) as response:
        data = json.load(response)
        return data, dict(response.headers.items())


def get_releases(repository: str, token: str | None) -> list[dict]:
    releases: list[dict] = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repository}/releases?per_page=100&page={page}"
        payload, _ = github_get(url, token)
        if not isinstance(payload, list):
            raise RuntimeError("GitHub Releases API returned an unexpected response")
        releases.extend(item for item in payload if isinstance(item, dict))
        if len(payload) < 100:
            return releases
        page += 1


def root_game_names(readme: str) -> dict[str, str]:
    names: dict[str, str] = {}
    pattern = re.compile(
        r"^\|\s*(?P<name>.*?)\s*\|.*?\[查看\]\(games/(?P<slug>[^/)]+)/?\)\s*\|\s*$",
        re.MULTILINE,
    )
    for match in pattern.finditer(readme):
        name = re.sub(r"[*_`]", "", match.group("name")).strip()
        names[unquote(match.group("slug"))] = name
    return names


def game_catalog(readme: str, repository: str) -> list[dict]:
    names = root_game_names(readme)
    release_pattern = re.compile(
        rf"https://github\.com/{re.escape(repository)}/releases/tag/([^\s)\"'<>]+)",
        re.IGNORECASE,
    )
    cover_pattern = re.compile(
        rf"{re.escape('<!-- game-cover:start -->')}.*?<img\s+[^>]*src=[\"']([^\"']+)[\"']",
        re.IGNORECASE | re.DOTALL,
    )
    catalog: list[dict] = []
    for game_readme in sorted(GAMES_PATH.glob("*/README.md")):
        text = game_readme.read_text(encoding="utf-8-sig")
        cover_match = cover_pattern.search(text)
        tags = sorted({unquote(tag.rstrip("/")) for tag in release_pattern.findall(text)})
        if not cover_match or not tags:
            continue
        slug = game_readme.parent.name
        title = names.get(slug)
        if not title:
            heading = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
            title = heading.group(1).strip() if heading else slug.replace("-", " ")
            title = re.sub(r"\s+简体中文(?:汉化|补丁).*$", "", title).strip()
        catalog.append(
            {
                "slug": slug,
                "title": title,
                "cover": cover_match.group(1),
                "tags": tags,
            }
        )
    return catalog


def rank_games(catalog: list[dict], releases: list[dict]) -> list[dict]:
    tag_owners: dict[str, list[str]] = defaultdict(list)
    for game in catalog:
        for tag in game["tags"]:
            tag_owners[tag].append(game["slug"])

    release_by_tag = {
        item.get("tag_name"): item
        for item in releases
        if item.get("tag_name") and not item.get("draft") and not item.get("prerelease")
    }
    ranked: list[dict] = []
    for game in catalog:
        owned_releases = []
        for tag in game["tags"]:
            if len(tag_owners[tag]) != 1:
                continue
            release = release_by_tag.get(tag)
            if release:
                owned_releases.append(release)
        if not owned_releases:
            continue
        downloads = sum(
            int(asset.get("download_count", 0))
            for release in owned_releases
            for asset in release.get("assets", [])
            if isinstance(asset, dict)
        )
        newest = max(
            owned_releases,
            key=lambda release: release.get("published_at") or release.get("created_at") or "",
        )
        update_times = [
            release.get("published_at") or release.get("created_at") or ""
            for release in owned_releases
        ]
        update_times.extend(
            asset.get("updated_at") or asset.get("created_at") or ""
            for release in owned_releases
            for asset in release.get("assets", [])
            if isinstance(asset, dict)
        )
        ranked.append(
            {
                **game,
                "downloads": downloads,
                "release_url": newest.get("html_url"),
                "updated_at": max(update_times, default=""),
            }
        )
    ranked.sort(key=lambda game: (-game["downloads"], game["title"].casefold()))
    return ranked


def render_cards(games: list[dict], detail_text) -> str:
    if len(games) < TOP_N:
        raise RuntimeError(
            f"Only {len(games)} unambiguous game releases were found; {TOP_N} are required"
        )
    rows = []
    for row_start in range(0, TOP_N, 5):
        cells = []
        for rank, game in enumerate(
            games[row_start : row_start + 5], start=row_start + 1
        ):
            title = html.escape(game["title"])
            cover = html.escape(game["cover"], quote=True)
            game_url = html.escape(f"games/{quote(game['slug'])}/", quote=True)
            cells.append(
                "    <td align=\"center\" width=\"20%\">\n"
                f"      <a href=\"{game_url}\"><img src=\"{cover}\" alt=\"{title} 游戏封面\" width=\"180\"></a><br>\n"
                f"      <strong>{rank}. {title}</strong><br>\n"
                f"      <sub><a href=\"{game_url}\">{html.escape(detail_text(game))}</a></sub>\n"
                "    </td>"
            )
        rows.append("  <tr>\n" + "\n".join(cells) + "\n  </tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def render_block(games: list[dict]) -> str:
    return (
        f"{START_MARKER}\n"
        "## 总下载量前十\n\n"
        + render_cards(
            games,
            lambda game: f"查看详情（{game['downloads']:,} 次下载）",
        )
        + "\n"
        f"{END_MARKER}"
    )


def render_recent_block(games: list[dict]) -> str:
    recent = sorted(
        games,
        key=lambda game: (game["updated_at"], game["title"].casefold()),
        reverse=True,
    )[:TOP_N]
    return (
        f"{RECENT_START_MARKER}\n"
        "## 最近更新\n\n"
        + render_cards(recent, lambda _game: "查看详情")
        + "\n"
        f"{RECENT_END_MARKER}"
    )


def replace_recent_block(readme: str, block: str) -> str:
    old_start = "<!-- monthly-downloads:start -->"
    old_end = "<!-- monthly-downloads:end -->"
    if readme.count(old_start) != readme.count(old_end):
        raise RuntimeError("README contains an incomplete monthly-downloads marker block")
    if old_start in readme:
        pattern = re.compile(
            rf"{re.escape(old_start)}.*?{re.escape(old_end)}",
            re.DOTALL,
        )
        return pattern.sub(block, readme, count=1)
    if readme.count(RECENT_START_MARKER) != readme.count(RECENT_END_MARKER):
        raise RuntimeError("README contains an incomplete recent-updates marker block")
    if RECENT_START_MARKER in readme:
        pattern = re.compile(
            rf"{re.escape(RECENT_START_MARKER)}.*?{re.escape(RECENT_END_MARKER)}",
            re.DOTALL,
        )
        return pattern.sub(block, readme, count=1)
    download_heading = re.search(r"^## 下载(?:\s|$)", readme, re.MULTILINE)
    if not download_heading:
        raise RuntimeError("Could not find the root README download heading")
    return readme[: download_heading.start()] + block + "\n\n" + readme[download_heading.start() :]


def replace_block(readme: str, block: str) -> str:
    if readme.count(START_MARKER) != readme.count(END_MARKER):
        raise RuntimeError("README contains an incomplete top-downloads marker block")
    if START_MARKER in readme:
        pattern = re.compile(
            rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
            re.DOTALL,
        )
        return pattern.sub(block, readme, count=1)
    download_heading = re.search(r"^## 下载(?:\s|$)", readme, re.MULTILINE)
    if not download_heading:
        raise RuntimeError("Could not find the root README download heading")
    return readme[: download_heading.start()] + block + "\n\n" + readme[download_heading.start() :]


def main() -> int:
    repository = os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPOSITORY)
    token = os.environ.get("GITHUB_TOKEN")
    readme = README_PATH.read_text(encoding="utf-8-sig")
    catalog = game_catalog(readme, repository)
    releases = get_releases(repository, token)
    top_games = rank_games(catalog, releases)
    updated = replace_block(readme, render_block(top_games[:TOP_N]))
    updated = replace_recent_block(updated, render_recent_block(top_games))
    if updated != readme:
        README_PATH.write_text(updated, encoding="utf-8", newline="\n")
        print("Updated README.md")
    else:
        print("README.md is already up to date")
    for rank, game in enumerate(top_games[:TOP_N], start=1):
        print(f"total {rank}. {game['title']}: {game['downloads']} downloads")
    recent_games = sorted(
        top_games,
        key=lambda game: (game["updated_at"], game["title"].casefold()),
        reverse=True,
    )[:TOP_N]
    for rank, game in enumerate(recent_games, start=1):
        print(f"recent {rank}. {game['title']}: {game['updated_at']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
