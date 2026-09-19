# Midnight News Report 简体中文汉化（120 FPS）

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4894100/Midnight_News_Report/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4894100/0d935314f696690010007f529440878d281a37c0/header.jpg?t=1789585726" alt="Midnight News Report 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

## 发布信息

- **适用版本：** Steam Windows 版 `BuildID 25404154`（2026-09-19 更新）
- **Steam AppID：** `4894100`
- **游戏引擎：** Unity 2022.3.10f1 Mono
- **补丁技术：** Unity 静态资源与托管程序集替换
- **帧率修改：** GameSettings 默认值与三个场景实例由 60 FPS 调整为 120 FPS
- **Release 文件：** `Midnight-News-Report-Simplified-Chinese-120FPS.zip`
- **文件大小：** 42,504,316 字节
- **SHA-256：** `2EEC56DAB1946F036816B93ACFC47CC4A385CFAB7070E614F30972A88F24649E`
- **压缩包文件数量：** 13
- **发布状态：** 已发布
- **下载地址：** [Midnight News Report 简体中文汉化（120 FPS）](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/midnight-news-report-cn-20260917)

## 汉化内容

本补丁汉化游戏文本、关键场景图像与 12 张玫瑰解谜电视图。颜色词与对应含义按游戏对话和解谜关系处理。主菜单含透明青蛙头署名徽标，进入游戏场景后自动消失。

## 2026-09-19 更新

- 依据当前 `BuildID 25404154` 的官方资源重新迁移全部汉化内容，修复旧包覆盖更新版后无法启动的问题。
- 重新映射更新后变化的 Unity 对象与 PathID，并完成资源、程序集、字体、贴图和 120 FPS 修改的静态回读。
- 游戏目录 12 个目标文件哈希一致；303 个场景文本字段、22 个动态程序集文本和 22 张文字贴图通过回读校验。

## 安装说明

1. 完全退出游戏。
2. 备份游戏目录内将被覆盖的同名文件。
3. 将压缩包内容解压到包含游戏主程序的根目录，按原目录层级覆盖同名文件。
4. 从 Steam 正常启动游戏并手动检查中文显示、解谜提示与帧率表现。

## 卸载说明

恢复安装前备份的同名文件；也可通过 Steam 验证游戏文件完整性恢复官方资源。验证完整性会移除本补丁修改。

## 兼容性说明

- 本补丁直接修改 Unity 资源与托管程序集，游戏更新后可能失效或不兼容。
- 当前覆盖包仅保证与 Steam `BuildID 25404154` 的资源结构匹配。
- 不含 BepInEx、Doorstop、Harmony、自动翻译器或 DLL 代理。
- 不建议与其他修改相同资源或 `Assembly-CSharp.dll` 的补丁混用。
- 本补丁不能独立运行，必须配合合法取得的完整原版游戏使用。

## 静态校验

- ZIP 可正常列出，共 13 个条目。
- 顶层内容为 `Midnight News Report_Data` 与 `汉化说明.txt`。
- Unity 对象解析数为 22,216，解析错误为 0；文本、贴图、程序集和三个场景 120 FPS 值均完成静态回读。
- 发布附件大小与本地成品一致，GitHub Release 附件与本页 SHA-256 一致。

## 验证声明

本次只完成文件结构、哈希与发布状态静态校验，没有启动游戏。实际中文显示、解谜对应关系、120 FPS 效果与当前游戏版本兼容性仍需用户手动验证。

本汉化为非官方免费补丁，不得倒卖；转载时请保留“Cokepoetry 汉化”署名，并配合合法取得的完整原版游戏使用。
