**Steam 版本回退（Build 26527345）：** **`download_depot 3370490 3370492 6322648434907831984`** · [核对 SteamDB Depot](https://steamdb.info/app/3370490/depots/) · [操作教程](../../README.md#steam-游戏版本回退)

# Giggleland（危笑乐园）简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/3370490/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3370490/b11309f0d80c4e425b070dbaafd45acdf3b8e33b/header_alt_assets_0.jpg?t=1794319433" alt="Giggleland 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

## 发布信息

- 正式名称：Giggleland，Steam AppID **3370490**，开发商 Hooked，发行商 Gamincat, Inc.。「危笑乐园」是本补丁采用的民间译名。
- 版本：**汉化 v1.1（开门卡关修复）**。仅适用 Windows Steam **Build 26527345 / 游戏 v1.1.0**。
- 引擎及补丁形式：**Unity 2022.3.62f2 / IL2CPP，xdelta3 静态二进制差分**，无需运行时注入。
- 附件：`Giggleland_CN_v1.1_Build26527345.zip`，**386,341,763 字节（约 368.44 MiB）**，共 **39** 个文件。
- SHA-256：`4a4ef87e4b022f9cac15f4b913b62980b8d7d4c2e04add3514f1bcd6a9b24b23`。
- [前往 GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/giggleland-cn-20261111) 下载标为「v1.1 修复版」的附件。旧版 v1.0 有卡关问题，不建议使用。

## v1.1 修复

修复泰瑞之家车库段落在「是我创造了你！」之后无法推进开门的问题。恢复六个场景中误被翻译的 105 处对白和剧情触发标记，保留中文字幕，不修改原有开门条件、游戏程序或存档。

## 汉化内容

包含界面、对白字幕、任务与交互提示、笔记、钥匙名称及环境贴图汉化；保留大字纸条排版和主菜单汉化署名。收录了游玩反馈中的广播与电视字幕、展示台任务、笔记日期和转录提示、风车钥匙等漏译修订。

部分故障画面、磨损小字、动态状态贴图以及一张未处理的告示保留原样。不包含中文配音，不把静态核查当作全流程无漏译的保证。

## 安装与还原

1. 完全退出游戏。已装 v1.0 差分版的玩家先用旧包的 `Restore_Original.cmd` 还原。若没有原版备份，或用过手动覆盖版，请在 Steam 验证游戏文件完整性，并确认恢复到匹配的 Build 26527345。游戏所在磁盘建议至少预留 **10 GiB**。
2. 将 ZIP 全部内容解压到 `Giggleland.exe` 所在的游戏目录，保留 `Giggleland_ChinesePatch` 文件夹结构。
3. 双击 `Install_CN.cmd`，等待出现 `Success: Install`。安装器先校验原版并自动备份，再重建与核验全部文件；无需另外切换语言。安装时不要启动或更新游戏。
4. 要卸载，退出游戏后双击 `Restore_Original.cmd`。备份在 `Giggleland_ChinesePatch/Backup`；备份缺失或游戏已更新时，使用 Steam 验证文件完整性。

只支持清单所列的匹配原版。版本或文件哈希不符时安装器会停止；游戏更新后请勿强行套用。本包不修改存档、按键、帧率或分辨率。

## 校验与反馈

已核验 ZIP，并从原版重建 **29** 个文件逐一核对 SHA-256。公开包不含游戏主程序、完整原版资源容器或原版字体文件；安装器使用玩家本机的原版数据。已用隔离原版副本验证安装和还原，未自动启动游戏。反馈时请附游戏 BuildID、补丁版本、章节位置、触发步骤和截图，能提供原文或日志更好。

本补丁为非官方免费汉化，不得倒卖。必须配合合法取得的完整原版游戏使用。
