import unittest

import update_top_downloads as catalog


class ReleaseVisibilityTests(unittest.TestCase):
    def test_game_names_accept_nonbreaking_detail_links(self):
        readme = "| Poop Killer（大便杀手） | Cokepoetry | 已发布 | 覆盖包 | [查&#8288;看](games/Poop-Killer/) |"
        self.assertEqual(catalog.root_game_names(readme), {"Poop-Killer": "Poop Killer（大便杀手）"})

    def test_refresh_can_keep_existing_recent_position(self):
        games = [{"slug": "Sunnybrook", "title": "Sunnybrook", "cover": "cover.png",
                  "tags": ["sunny"], "recent_update_at": "2026-11-02T03:02:56Z"}]
        releases = [{"tag_name": "sunny", "draft": False, "prerelease": False,
                     "published_at": "2026-10-28T00:00:00Z", "assets": [
                         {"download_count": 2, "updated_at": "2026-11-02T12:00:00Z"}]}]
        ranked = catalog.rank_games(games, releases)
        self.assertEqual(ranked[0]["updated_at"], "2026-11-02T03:02:56Z")
        self.assertEqual(ranked[0]["downloads"], 2)

    def setUp(self):
        self.games = [
            {"slug": "Meat-Train", "title": "MEAT TRAIN", "cover": "cover.png", "tags": ["meat-test"]},
            {"slug": "Stable", "title": "Stable", "cover": "stable.png", "tags": ["stable"]},
            {"slug": "Draft", "title": "Draft", "cover": "draft.png", "tags": ["draft"]},
        ]
        self.releases = [
            {"tag_name": "meat-test", "prerelease": True, "draft": False,
             "published_at": "2026-10-23T11:00:00Z",
             "assets": [{"download_count": 5, "updated_at": "2026-10-23T15:00:00Z"}]},
            {"tag_name": "stable", "prerelease": False, "draft": False,
             "published_at": "2026-10-22T11:00:00Z", "assets": [{"download_count": 8}]},
            {"tag_name": "draft", "prerelease": True, "draft": True,
             "published_at": "2026-10-24T11:00:00Z", "assets": []},
        ]

    def test_download_ranking_keeps_existing_stable_only_policy(self):
        ranked = catalog.rank_games(self.games, self.releases)
        self.assertEqual([g["slug"] for g in ranked], ["Stable"])
        self.assertEqual(ranked[0]["downloads"], 8)

    def test_recent_candidates_include_public_prereleases_but_not_drafts(self):
        ranked = catalog.rank_games(self.games, self.releases, include_prereleases=True)
        self.assertEqual({g["slug"] for g in ranked}, {"Meat-Train", "Stable"})
        meat = next(g for g in ranked if g["slug"] == "Meat-Train")
        self.assertTrue(meat["prerelease"])
        self.assertEqual(meat["updated_at"], "2026-10-23T15:00:00Z")

    def test_recent_card_labels_test_version_and_sorts_by_asset_update(self):
        games = catalog.rank_games(self.games, self.releases, include_prereleases=True)
        games.extend(
            {"slug": f"Older-{i}", "title": f"Older {i}", "cover": "old.png",
             "updated_at": "2026-10-01T00:00:00Z", "prerelease": False}
            for i in range(8)
        )
        block = catalog.render_recent_block(games)
        self.assertIn("1. MEAT TRAIN", block)
        self.assertIn("查看详情（测试版）", block)
        self.assertLess(block.index("MEAT TRAIN"), block.index("Stable"))

    def test_ambiguous_release_ownership_is_still_excluded(self):
        games = self.games + [{**self.games[0], "slug": "Duplicate"}]
        ranked = catalog.rank_games(games, self.releases, include_prereleases=True)
        self.assertEqual([g["slug"] for g in ranked], ["Stable"])


if __name__ == "__main__":
    unittest.main()
