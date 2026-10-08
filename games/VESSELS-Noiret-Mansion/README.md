# VESSELS: Noiret Mansion 简体中文汉化（2026-10-08 更新修复版）

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4884960/VESSELS_Noiret_Mansion/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4884960/a883d176f8c4f97ddfb304062487b29a9239762a/header.jpg?t=1790853435" alt="VESSELS: Noiret Mansion 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry / 5050 汉化组**

## 下载与版本

- **发布页面：** [GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/vessels-noiret-mansion-cn-v1.2-20261002)
- **当前附件：** [VESSELS 更新修复版 .7z](https://github.com/Linbin-Lai/5050-hanhua/releases/download/vessels-noiret-mansion-cn-v1.2-20261002/VESSELS-Noiret-Mansion-Simplified-Chinese-20261008.7z)
- **原始成品名：** `VESSELS Noiret Mansion修复.7z`。GitHub 附件仅改用英文文件名，内容不变。
- **文件大小：** 23,862,216 字节；7z 内有 7 个 Unity 资源文件和一份使用说明。
- **SHA-256：** `4F2714E791E57C6D0A261FB27D212281BEC41B878E1573B6D5370D106B4041D1`
- **适用范围：** 用户提供的 2026-10-08 更新修复资源；资源头为 Unity 6000.2.13f1。未附对应 Steam BuildID。

## 本次修复

此包针对游戏更新后旧版汉化覆盖包导致闪退的问题，改用更新后的 Unity 资源文件。包内 `resources.assets` 可静态读到简体中文界面和正文。旧版 ZIP 已从 Release 移除，**不要叠加安装旧版**。

新版只包含资源文件，不含旧版独立的 `Assembly-CSharp.dll`、`ChineseWatermark.dll`、青蛙图片或场景文件；不保证旧版菜单水印仍可显示，也不应把旧版这些文件加入新包。

## 安装

1. 完全退出游戏，备份存档和将被覆盖的游戏文件。
2. 如果装过旧版 v1.2 ZIP，先通过 Steam 验证游戏文件完整性，恢复它修改过的 `level1`、`Assembly-CSharp.dll`、`ScriptingAssemblies.json`、`sharedassets3.assets` 等文件；再删除旧包额外添加的 `VESSELS Noiret Mansion_Data/Managed/ChineseWatermark.dll` 与 `VESSELS Noiret Mansion_Data/5050_watermark_frog.png`。验证完整性不一定会删除额外文件。
3. 将 7z 中的七个资源文件直接放到游戏的 `VESSELS Noiret Mansion_Data` 目录，允许覆盖同名文件。压缩包顶层没有 `VESSELS Noiret Mansion_Data` 文件夹，不要解压到游戏 EXE 所在的上一级目录。
4. 启动游戏并检查中文显示。若游戏仍闪退，请附游戏版本、安装方式和错误日志反馈。

卸载时通过 Steam 验证游戏文件完整性，或恢复安装前备份的同名文件。

## 验证范围

已验证 7z 可完整解压、文件数量与路径、资源头及附件哈希；未进行实机启动或完整流程测试，因此不能独立确认所有更新场景都不再闪退。本补丁不能独立运行，必须配合合法取得的完整原版游戏使用。

本汉化为非官方免费补丁，不得倒卖；转载时请保留汉化署名与原游戏作者署名。
