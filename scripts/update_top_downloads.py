#!/usr/bin/env python3
"""Update the root README with the five most-downloaded game releases."""

from __future__ import annotations

import html
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
GAMES_PATH = ROOT / "games"
START_MARKER = "<!-- top-downloads:start -->"
END_MARKER = "<!-- top-downloads:end -->"
DEFAULT_REPOSITORY = "Linbin-Lai/5050-hanhua"


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
        ranked.append(
            {
                **game,
                "downloads": downloads,
                "release_url": newest.get("html_url"),
            }
        )
    ranked.sort(key=lambda game: (-game["downloads"], game["title"].casefold()))
    return ranked[:5]


def render_block(games: list[dict]) -> str:
    if len(games) < 5:
        raise RuntimeError(f"Only {len(games)} unambiguous game releases were found; five are required")
    cells = []
    for rank, game in enumerate(games, start=1):
        title = html.escape(game["title"])
        cover = html.escape(game["cover"], quote=True)
        release_url = html.escape(game["release_url"], quote=True)
        downloads = f"{game['downloads']:,}"
        cells.append(
            "    <td align=\"center\" width=\"20%\">\n"
            f"      <a href=\"{release_url}\"><img src=\"{cover}\" alt=\"{title} 游戏封面\" width=\"180\"></a><br>\n"
            f"      <strong>{rank}. {title}</strong><br>\n"
            f"      <a href=\"{release_url}\">下载（{downloads} 次）</a>\n"
            "    </td>"
        )
    return (
        f"{START_MARKER}\n"
        "## 下载量前五\n\n"
        "<p align=\"center\">按可明确归属到单个游戏的 GitHub Release 附件累计下载量每日自动更新。</p>\n\n"
        "<table>\n"
        "  <tr>\n"
        + "\n".join(cells)
        + "\n  </tr>\n"
        "</table>\n"
        f"{END_MARKER}"
    )


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
    updated = replace_block(readme, render_block(top_games))
    if updated != readme:
        README_PATH.write_text(updated, encoding="utf-8", newline="\n")
        print("Updated README.md")
    else:
        print("README.md is already up to date")
    for rank, game in enumerate(top_games, start=1):
        print(f"{rank}. {game['title']}: {game['downloads']} downloads")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
