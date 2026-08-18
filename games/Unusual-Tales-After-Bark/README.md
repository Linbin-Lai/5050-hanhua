# Unusual Tales: After Bark 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4516880/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4516880/1a00f0306b6506b19b27984a971f266af2e3f6c5/header.jpg?t=1786737888" alt="Unusual Tales: After Bark 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

## 发布信息

- Steam AppID：`4516880`
- 游戏版本：2026-08-18 制作时的 Windows 64 位 Steam 版本（BuildID 未记录）
- 游戏引擎：Unity 2021.3.25f1，Windows x86-64，Mono
- 补丁技术：静态 Unity 资源、Localization 表与 `Assembly-CSharp.dll` 精确字符串替换
- Release 文件：`Unusual Tales After Bark_简体中文覆盖包.zip`
- 文件大小：31,183,075 字节
- SHA-256：`96DFB4F1CA797B3D1439FE9413B06ADB1578017821D73ED7D0063D46E506C0D5`
- 压缩包文件数量：12
- 发布状态：待发布
- 下载地址：[GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/unusual-tales-after-bark-cn-20260818)

> 附件不能独立运行，必须配合用户从 Steam 合法取得的完整原版游戏使用。

## 汉化内容

- 四个原有语言槽中的程序文本均替换为简体中文，静态回读共 547 个程序文本候选。
- 嵌入 Noto Sans CJK SC 字体资源，覆盖翻译所需的 872 个唯一汉字。
- 已处理主菜单、汉化署名、重要路牌、警告、广告及环境文字，共修改 15 张图片、16 个区域。
- 沿用游戏原生字幕系统，没有加入可能重复显示或抢占原字幕的额外字幕框。
- 游戏内约 17 分钟的低分辨率电视节目仍保留体验级英文广告小字，未进行可能损坏画质和兼容性的破坏性重编码。
- 36 条缺少静态本地化键的环境语音无法证明已绑定原生字幕，其中 3 条属于关键静态风险；本版未强行注入重复字幕。

## 安装说明

1. 完全退出游戏。
2. 备份可能被覆盖的游戏资源。
3. 将覆盖包内全部文件解压到含 `Unusual Tales After Bark.exe` 的游戏根目录。
4. 允许合并目录并覆盖同名文件。
5. 正常启动游戏并保持原生显示设置；四个原有语言槽均已构建中文文本。

## 卸载说明

在 Steam 客户端中验证游戏文件完整性，以恢复被覆盖的原始资源。

## 兼容性说明

- 适用于本补丁制作时扫描到的 Windows 64 位、Unity 2021.3.25f1 Mono 版本。
- 可直接安装到未安装任何汉化工具的对应纯英文原版，不需要 BepInEx、Unity 编辑器或第三方字体。
- 本补丁会覆盖派生游戏资源；游戏更新导致原文件变化后，请勿继续沿用旧补丁，应等待重新构建。
- 未记录 Steam BuildID，因此安装前应以发布日期、游戏引擎版本和包内安装说明共同核对兼容性。

## 静态校验

- ZIP 可正常读取，共 12 个文件；第一层仅包含 `Unusual Tales After Bark_Data` 与 `安装说明.txt`。
- 9 个 Unity 容器或资源文件均可重新解析，`Assembly-CSharp.dll` 回读通过。
- 四个 Localization 语言包各包含 544 条中文记录，目录 CRC 与文件大小已同步修正。
- ZIP 内 12/12 文件与构建目录 SHA-256 一致；静态构建错误、警告与资源回封失败均为 0。
- 未包含游戏主程序、BepInEx、日志、缓存、备份、源码、`obj`、`pdb` 或调试文件。

## 反馈要求

反馈时请提供游戏版本、补丁 SHA-256、问题截图、所在位置、前后流程、可见原文及相关日志。语音问题还请说明说话人、场景和大致触发时间。

## 验证声明

本次仅完成静态解析、构建、资源回读、同步与哈希检查；没有启动游戏。中文字体、排版、署名、低概率语音及实际流程仍需用户手动验证。
