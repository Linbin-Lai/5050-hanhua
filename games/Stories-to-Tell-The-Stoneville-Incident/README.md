# [Stories to Tell] The Stoneville Incident 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4835250/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4835250/e5cf0b0a8ef24ccdab5946fd628169db435f9a66/header.jpg?t=1784048465" alt="[Stories to Tell] The Stoneville Incident 简体中文汉化 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

## 发布信息

- 引擎/架构：Unreal Engine 5.6（Windows x64，CL-44394996）
- Release 文件：`Stoneville.Incident.Simplified.Chinese.Patch.zip`
- 文件大小：1720965 字节
- ZIP SHA-256：`234C85D5A3BA8D90213220ED3273010E698D536ABEEE79FEBC009BD4C4AD4DE6`
- ZIP 文件数：5
- 发布审查状态：`published`
- 下载地址：[GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/stories-to-tell-stoneville-incident-cn-20260816)

> 附件不能独立运行，必须配合用户从 Steam 合法取得的完整原版游戏使用。

## 安装说明

1. 完全退出游戏。
2. 将 ZIP 内全部文件覆盖到游戏的 `Windows` 根目录。
3. 从游戏原生入口正常启动，不需要安装额外汉化工具或第三方字体。

卸载时只删除以下三个补丁文件，不要删除原版主容器：

```text
Windows\StoriesToTell\Content\Paks\StoriesToTell_Chinese_P.pak
Windows\StoriesToTell\Content\Paks\StoriesToTell_Chinese_P.utoc
Windows\StoriesToTell\Content\Paks\StoriesToTell_Chinese_P.ucas
```

## 汉化内容

- 使用高优先级 Unreal PAK / IoStore 补丁，不覆盖原始 PAK、UTOC 或 UCAS。
- 包含程序文本汉化及已确认的重要视觉文字。
- 保留游戏原生字幕系统，不额外叠加独立字幕框或运行时字幕组件。
- 补丁容器与原版容器联合挂载静态检查通过。

## 静态校验

- ZIP 可正常读取，共 5 个文件，包含匹配的 `.pak`、`.utoc` 和 `.ucas` 三件套。
- 原版与补丁 combined dry-run 共验证 3408 个资产，失败数为 0。
- GitHub 远端附件大小与本地一致，Release 记录的 SHA-256 与本页一致。
- 未包含游戏主程序、原始主容器、日志、缓存或调试文件。

## 反馈要求

反馈时请提供游戏版本、补丁 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

本次仅完成静态容器、联合挂载、资源结构、回读和哈希检查；没有启动游戏，实际中文显示与流程由用户手动验证。
