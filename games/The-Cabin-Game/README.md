# the cabin game 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4406280/the_cabin_game/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4406280/d3cad021841c8731a0da86e0a0b1321df341cfd0/header.jpg?t=1787842454" alt="the cabin game 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

> 本版为 2026-09-02 发布的 UE5.5 IoStore 修复版，替代 2026-08-30 的旧式 PAK + UE4SS 版本。

## 发布信息

- **适用版本：** Steam AppID 4406280，基于 2026-09-02 本机已安装的 UE5.5 版本资源构建（包内未记录 BuildID）
- **游戏引擎：** Unreal Engine 5.5
- **补丁技术：** Unreal PAK + IoStore UTOC/UCAS 覆盖容器
- **Release 文件：** `the-cabin-game-Chinese-localization.zip`
- **文件大小：** 19,042,305 字节
- **SHA-256：** `19042914043EC6E06A9B2E80450B120BA60EF2AFB81CBDB9A16F4DF7FDBB6E14`
- **压缩包文件数量：** 4
- **发布状态：** 已发布
- **下载地址：** [the cabin game 简体中文汉化 v2（UE5.5 IoStore 修复版）](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/the-cabin-game-cn-20260830)

## 汉化内容

- 传统 PAK 承载本地化 LocRes 与字体资源。
- 配套 UTOC/UCAS 覆盖设置表、商店表和相关控件文本。
- 修复旧式 PAK 无法覆盖当前 IoStore 资源的问题。

压缩包说明未声明所有低频或更新后新增文本均已验证，因此本页不对实际完整度作超出静态证据的承诺。

## 安装说明

1. 完全退出游戏。
2. 如果从 2026-08-30 旧版升级，请先删除旧补丁留下的 `the_cabin_game\Binaries\Win64\dwmapi.dll` 和 `the_cabin_game\Binaries\Win64\ue4ss` 目录；不要删除游戏原有文件。
3. 备份 `the_cabin_game\Content\Paks` 中可能被覆盖的同名汉化文件。
4. 将新版 ZIP 内全部内容复制到包含游戏主程序的根目录，选择合并目录并覆盖同名汉化文件。
5. 确认以下三个文件同时存在：
   - `the_cabin_game\Content\Paks\the_cabin_game_Chinese_P.pak`
   - `the_cabin_game\Content\Paks\the_cabin_game_Chinese_P.utoc`
   - `the_cabin_game\Content\Paks\the_cabin_game_Chinese_P.ucas`
6. 无需选择特定语言；从 Steam 正常启动游戏。
7. 三个补丁文件必须保持同名并成套安装，首次启动后请检查菜单、设置、商店和剧情文字。

## 卸载说明

删除上述三个 `the_cabin_game_Chinese_P` 文件即可。不要删除游戏原有的 `the_cabin_game-Windows` 或 `global` 容器；如安装过 2026-08-30 旧版，还应删除其 `dwmapi.dll` 和 `ue4ss` 目录。必要时可通过 Steam 验证游戏文件完整性。

## 兼容性说明

- 基于 2026-09-02 本机已安装的 UE5.5 版本资源构建，包内未记录明确 BuildID。
- 本版以 PAK、UTOC、UCAS 三件套适配当前 IoStore 资源结构，不再依赖 UE4SS。
- 游戏更新后如资源版本或 IoStore 结构变化，可能需要重新适配。
- 本补丁不能独立运行，必须配合合法取得的完整原版游戏使用。

## 历史版本

2026-08-30 版本使用旧式 PAK + UE4SS 运行时修正，文件大小 23,485,979 字节，SHA-256 为 `55BD2598D506C084BE996270C5E3095894225732B8246FC52624F0834ABA7309`。该旧附件已由本版替换，不应继续使用。

## 静态校验

- ZIP 压缩包可正常读取，共 4 个文件；第一层为 `安装说明.txt` 和 `the_cabin_game/`。
- 压缩包大小为 19,042,305 字节，SHA-256 为 `19042914043EC6E06A9B2E80450B120BA60EF2AFB81CBDB9A16F4DF7FDBB6E14`。
- `the_cabin_game_Chinese_P.pak`：19,263,515 字节，SHA-256 `5E313407281B34B888BC6290A421FF6A84724167E750E2954D6C47B72395B252`。
- `the_cabin_game_Chinese_P.ucas`：43,594 字节，SHA-256 `6B7AA623FFEC3612B42E1582754FB8DB1DC5897A68C4AD006F33B90BD83FED27`。
- `the_cabin_game_Chinese_P.utoc`：1,036 字节，SHA-256 `366C12878CD31C93D17D5B2072288C1C7798DC754FF320AA10ACBF1CFC66BF92`。
- 未发现完整游戏主程序、DLL、日志、存档、缓存、源码、OBJ、PDB、调试文件、完整商业字体、音频或视频。

## 反馈要求

请在 Issue 中提供游戏版本、BuildID、补丁版本、问题截图、出现位置、前后流程、日志和可见原文，以便定位。

## 验证声明

本次只完成压缩包结构、文件读取和哈希静态校验，没有启动游戏。实际中文显示、交互流程与当前版本兼容性仍需用户手动验证。

本汉化为非官方免费补丁，不得倒卖；必须配合合法取得的完整原版游戏使用。
