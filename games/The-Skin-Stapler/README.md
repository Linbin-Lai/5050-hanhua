# The Skin Stapler（缝皮杀手）简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4310610/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4310610/5147848411ce0dfd06d88513572a98e334a3fd74/header.jpg?t=1786367666" alt="The Skin Stapler 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：qsefthuopq**

## 发布信息

- 游戏版本：制作时的 Steam Windows 正式版（BuildID 未提供）
- 游戏引擎：Unreal Engine（精确版本未提供）
- 补丁技术：Unreal PAK / IoStore 高优先级覆盖容器
- Release 文件：`TheSkinStapler缝皮杀手汉化补丁.zip`
- 文件大小：5,460,111 字节
- SHA-256：`DA9A09FF6AF1D393A6FB938F5A8904E8CAD3F6AC24877B71160842CD095A10BE`
- 压缩包文件数量：3
- 发布状态：待发布
- 下载地址：[GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/the-skin-stapler-cn-20260825)

## 汉化内容

本补丁提供《The Skin Stapler》的简体中文本地化资源。压缩包由匹配的一组 `.pak`、`.utoc` 和 `.ucas` 补丁容器组成；包内未附汉化范围清单，因此本页不对具体界面、剧情、字幕或图片的完成度作超出静态证据的承诺。

## 安装说明

1. 完全退出游戏。
2. 备份 `TheSkinStapler\Content\Paks` 中可能存在的同名文件。
3. 将压缩包内三个文件解压到游戏目录下的 `TheSkinStapler\Content\Paks`。
4. 如系统提示存在同名文件，请先确认它来自本补丁的旧版本，再选择覆盖。
5. 本补丁不要求切换游戏语言；按游戏原有方式启动即可。
6. 首次启动后请手动检查主菜单、剧情文本、字幕和中文字体显示。

## 卸载说明

从 `TheSkinStapler\Content\Paks` 删除以下三个新增补丁文件：

- `TheSkinStapler-Windows_P.pak`
- `TheSkinStapler-Windows_P.utoc`
- `TheSkinStapler-Windows_P.ucas`

如曾覆盖同名旧补丁，请恢复安装前备份；必要时可通过 Steam 验证游戏文件完整性。

## 兼容性说明

- 面向 Steam AppID `4310610` 的 Windows 正式版，不适用于独立的 Demo AppID `4343530`。
- BuildID 未随补丁提供；游戏更新后若资源版本变化，可能出现汉化失效或启动异常。
- 适用于未安装其他汉化工具的原版游戏；与其他同名 PAK/IoStore 补丁混用可能发生挂载冲突。
- 补丁不能独立运行，必须配合合法取得的完整原版游戏使用。

## 静态校验

- ZIP 可正常列出并读取，共 3 个文件，第一层直接包含一组 PAK/IoStore 容器。
- 容器文件大小分别为：PAK 5,517,606 字节、UTOC 202 字节、UCAS 64 字节。
- 三个容器的 SHA-256 分别为：
  - PAK：`BF60A39CB31408AAB17366E65B31D6DE18CE70DF9F0BC830221A2F626F781F9A`
  - UTOC：`F84A24868938881ACD3B66C6960213B32AE46F850E4925893AF4A0079F951C88`
  - UCAS：`23FB59D9D7B91C7434F6C62E5EDF57EA7286F299404128A797F354F6DA1517ED`
- 未发现游戏主程序、可独立运行的完整游戏、日志、缓存、存档、源码、`obj`、`pdb`、音频、视频或字体文件。
- 包内没有安装说明或 BuildID 文件；该缺失已在兼容性说明中披露。

## 反馈要求

反馈时请提供游戏 BuildID、补丁文件 SHA-256、问题截图、出现位置、前后流程和可见原文。若游戏崩溃，请同时附完整错误提示以及 `Saved\Logs` 中的相关日志。

## 验证声明

本次发布只完成压缩包回读、文件结构、文件签名、哈希及禁止文件检查，没有启动游戏。实际中文显示、流程、字体和当前版本兼容性仍需用户手动验证。
