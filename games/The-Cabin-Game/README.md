# the cabin game 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4406280/the_cabin_game/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4406280/d3cad021841c8731a0da86e0a0b1321df341cfd0/header.jpg?t=1787842454" alt="the cabin game 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

> 本补丁为不完全汉化版本：少量文本未汉化，但不影响正常游玩。

## 发布信息

- **适用版本：** Steam AppID 4406280，适配 2026-08-29 的 Steam 抢先体验版本
- **游戏引擎：** Unreal Engine 4（Windows 64 位）
- **补丁技术：** Unreal PAK 静态资源覆盖 + UE4SS 运行时界面与设置项修正
- **Release 文件：** `the-cabin-game-Chinese-localization.zip`
- **文件大小：** 26,952,092 字节
- **SHA-256：** `BF5A30F5EF181C49DE45A3FE9D0AC99E6370C81E6771F59C881C9953DC55EBE0`
- **压缩包文件数量：** 16
- **发布状态：** 已发布（不完全汉化）
- **下载地址：** [the cabin game 简体中文汉化](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/the-cabin-game-cn-20260829)

## 汉化内容

- 汉化菜单、设置、玩法提示、游戏手册、商店及部分场景图片文字。
- 修正部分中文界面的字号与布局。
- 保留图片中的图标、符号和非文字内容。
- 未添加额外语音字幕系统。

本补丁不是完整汉化，仍有少量低频文本或更新后新增文本保留英文，但不影响正常游玩。

## 安装说明

1. 完全退出游戏。
2. 备份游戏目录中可能被覆盖的同名汉化文件。
3. 将覆盖包内全部文件复制到游戏根目录。
4. 系统询问时允许覆盖同名文件。
5. 从 Steam 正常启动游戏，无需手动切换语言。
6. 首次启动保持游戏原生显示和输入设置。

## 卸载说明

1. 删除游戏目录中的 `the_cabin_game\Binaries\Win64\dwmapi.dll`。
2. 删除 `the_cabin_game\Binaries\Win64\ue4ss` 目录。
3. 删除 `the_cabin_game\Content\Paks\the_cabin_game_Chinese_P.pak`。
4. 通过 Steam 验证游戏文件完整性以恢复原版。

## 兼容性说明

- 面向 Steam AppID 4406280 的 2026-08-29 抢先体验版本制作。
- 可直接安装到未安装汉化工具的原版游戏。
- 抢先体验版本更新可能新增文本，或改变资源结构与运行时界面，导致部分汉化失效。
- 本补丁为不完全汉化，少量文本未汉化但不影响正常游玩。

## 静态校验

- 覆盖包可正常读取，共 16 个文件，第一层为 `the_cabin_game/` 与 `安装说明.txt`。
- 覆盖包 SHA-256 为 `BF5A30F5EF181C49DE45A3FE9D0AC99E6370C81E6771F59C881C9953DC55EBE0`。
- 未发现完整游戏主程序、日志、存档、缓存、源码、PDB、调试文件、完整商业字体、音频或视频。
- 本次仅进行压缩包结构、文件读取和哈希静态校验，没有启动游戏。

## 反馈要求

请在 Issue 中提供游戏版本、补丁版本、问题截图、出现位置、前后流程和可见原文。若发生崩溃，请附完整错误信息与日志。

## 验证声明

本版完成了静态文件、脚本与压缩包结构校验。实际显示、交互流程和低概率文本仍需用户手动验证。

本汉化为非官方免费补丁，不得倒卖；必须配合合法取得的完整原版游戏使用。
