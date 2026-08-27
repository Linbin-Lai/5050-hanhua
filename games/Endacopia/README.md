# Endacopia 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/2684630/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2684630/8b5af90a03ce4cc33653c50a998387e3e9082103/header.jpg?t=1786381683" alt="Endacopia 简体中文汉化 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：** Cokepoetry 

## 发布信息

- 引擎/架构：Adventure Game Studio 3.6.0.55
- Release 文件：`Endacopia_简体中文覆盖包.zip`
- 文件大小：459078726 字节
- ZIP SHA-256：`FF52287FFAF924987F637E49587B285C6CEBCDA592BE00849D50F53531F39F7B`
- ZIP 文件数：25
- 发布审查状态：`published`
- 下载地址：[GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/endacopia-cn-20260806)

> 已公开发布。附件不能独立运行，必须配合用户从 Steam 合法取得的对应完整原版游戏使用；具体完成范围和已知问题仍以本页安装说明为准。

## 安装说明

```text
Endacopia 简体中文覆盖包
汉化署名：5050汉化组：Cokepoetry汉化

【适用版本】
Adventure Game Studio 3.6.0.55 引擎 / 32 位 / 游戏分辨率 384x216 / 游戏文本编码 UTF-8 (65001)
原始 Data\Endacopia.ags SHA-256:
F98C62833280C2A116BCCAFC94A64FDE0D9D75E5C8C61BB67E8CBF1D2A6C546B
游戏更新后请先核对该哈希，不一致时不要直接覆盖。

【安装】
1. 完全退出游戏。
2. 把压缩包内全部内容复制到 Endacopia 游戏根目录，合并 Windows 文件夹并覆盖同名文件。
3. 按原有方式启动游戏，保持游戏原生显示设置。
安装后 Windows\acsetup.cfg 的 [language] translation=Chinese 会启用中文；
也可以运行 winsetup.exe 在语言下拉框里手动切换。

【卸载】
删除 Windows 目录中本补丁加入的以下文件：
Chinese.tra、game28.dta、acsprset.spr、sprindex.dat、
agsfnt0.ttf 至 agsfnt6.ttf、FusionPixelFont-OFL.txt、校验清单.txt、
room4.crm、room5.crm、room6.crm、room9.crm、room11.crm、room12.crm、
room16.crm、room20.crm、room38.crm、room48.crm、room126.crm
然后把 acsetup.cfg 的 translation=Chinese 改回 translation= 。
这些都是松散覆盖文件；游戏本体 Endacopia.exe 与 Data\Endacopia.ags 未被修改，
删除后即可完全恢复英文原版。若不确定，也可在 Steam 里"验证游戏文件完整性"。

【技术方案】
- 采用 AGS 原生 .tra 翻译 + 松散资源覆盖。AGS 引擎 main.cpp 设置 kAssetPriorityDir，
  游戏目录内的松散文件优先于 Endacopia.exe 内嵌的 CLIB 资源，因此无需改动游戏本体。
- 不安装 BepInEx / Doorstop / Harmony / 自动翻译器，不注入任何运行时组件。
- Chinese.tra 共 7,986 条，UTF-8 编码，回读逐条一致。
- 七个字体槽使用随包提供的 Fusion Pixel Font 10px（SIL OFL 授权，见 FusionPixelFont-OFL.txt）。
```

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。
