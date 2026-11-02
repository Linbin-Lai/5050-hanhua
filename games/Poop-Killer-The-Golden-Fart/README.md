# Poop Killer - The Golden Fart 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/5173660/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/5173660/ac524212c21a5496dde13e365e85daa88a248265/header.jpg?t=1793394023" alt="Poop Killer - The Golden Fart 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

## 发布信息

- 正式名称：Poop Killer - The Golden Fart，Steam AppID **5173660**；开发商、发行商均为 **616 GAMES**。“大便杀手：黄金之屁”为本页民间译名。
- 适用版本：Windows x64，Steam **Build 26346415**；补丁 **v1.3**，2026-11-02。
- 引擎：Unity **2023.1.20f1 / IL2CPP**。
- 补丁形式：**静态 UnityFS 直接覆盖包，5个 ZIP 分卷，不是差分安装器**。
- 发布状态：**已发布（不完全汉化，部分装饰图片保留原文）**。
- 下载：[GitHub Release 发布页面](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/poop-killer-the-golden-fart-cn-20261102)。
- 完整 ZIP 名称：`Poop_Killer_The_Golden_Fart_CN_v1.3_Build26346415.zip`，**8,014,895,643 字节（约7.46 GiB）**，7个文件。
- 完整 ZIP SHA-256：`41df8ffa5b050250b12d89bbdc662838ed9aae55502f5e41da2e29557ac2a121`。
- 发布附件共7个：5个分卷、`READ_FIRST.txt`、`SHA256SUMS.txt`。包内根目录为 `Poop Killer - The Golden Fart_Data` 及许可、说明和校验资料。

| 分卷后缀 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `.zip.001` | 1992294400 | `0918a8e89f807144eca802596b827d93b8cc6585c70937f597e148d366cada97` |
| `.zip.002` | 1992294400 | `43e092aa742a8a6d3427700c520603c182c7a8c477b1ce17e30a7eb6eea65bba` |
| `.zip.003` | 1992294400 | `4abff282b996061806466ec69c3e95d7d415317976d70412e757be5ccb6ed44b` |
| `.zip.004` | 1992294400 | `dc72ab82ae4bcbf751826806f801a9b46d9f974bd7ef4f9ec7467c6057e31197` |
| `.zip.005` | 45718043 | `f2b2a965862413e9ca26d8907063213b721fb425f9ece048e64267be9ad2805d` |

## 汉化内容

3,778处文字字段、23张贴图、Noto中文字形和新游戏下方的小字署名。主要涉及菜单、对白、目标、交互、关键标牌、路线与小游戏图片；数字、密码、方向和图标不改。

包含启动时容器数据块兼容修复和退出时高位对象编号溢出修复。后者重排32个新增对象并修正84处引用；不是替换游戏主程序。v1.3将相关语境统一为“草／圣草／草卷”，保留“来点爽的”等表达，不改正常草药、画质、烟雾和普通物品语境。

微小包装细则、无法辨认的磨损小字、背景电视原片、电影海报及装饰涂鸦等保留原文，详见包内 `保留内容说明.txt`。原声和部分画面不作内容规避，不能保证直播适用性，不宣称全部图片零漏译。

## 安装说明

1. 下载完整的 `.zip.001` 至 `.zip.005` 共5卷，放在同一目录，保持文件名不变。
2. 使用7-Zip或Bandizip打开 `.zip.001` 并完整解压；**不要逐卷解压，也不要只下载第一卷**。
3. 完全退出游戏，备份原版 `Poop Killer - The Golden Fart_Data/data.unity3d` 和重要存档。安装前确认 Build 26346415。
4. 将解压后的 `_Data` 文件夹合并到含游戏 EXE 的根目录，替换同名 `data.unity3d`，不要多套一层目录。
5. 汉化使用原English槽，不增加语言选项；如果该槽标签已显示“简体中文”，选择该项即可。

安装、更新或退出前不要强制中断文件复制。本补丁不需要Python、插件、联网安装器或其他游戏的文件。

## 卸载与兼容

恢复自行备份的原版 `data.unity3d`，或在Steam验证完整性。更新游戏前先还原原版，不得将本包强行用于其他Build或混用旧版汉化。可用于相同Build的完整英文原版，不能独立运行，也不能代替购买原版游戏。

## 静态校验

发布用分卷已通过7-Zip完整性测试：5卷、7文件；公开版仅修订安装说明并分卷，游戏资源与本地v1.3逐字节一致。

7个线上附件均已回下载并重新计算SHA-256，与本地一致；按顺序拼接5卷所得ZIP的SHA-256也与上列完整ZIP校验值一致。

主文件 `data.unity3d`：8,014,883,048字节，SHA-256 `15977b437de5c679baa7c85059d3f34a75c6f4daeee7a03b0fb1270e1475d6da`。已扫描全部107,296个UnityFS解压块，未检出同类PEM私钥。不包含游戏EXE、GameAssembly、存档、无关缓存或运行时注入工具。

## 风险与验证声明

**完整容器带有大量未改动游戏音画及原内嵌字体，部分字体公开再分发许可未确认；公开提供不代表已取得原始素材的再分发授权。** 新增中文字形采用Noto Sans CJK SC，许可证随包。资源版权归各自权利人所有。

本次未自行启动游戏；静态校验不等于实际游戏测试。启动、菜单、开场对白、场景切换、路牌、小游戏及正常退出仍需玩家手动确认。

非官方、免费汉化，不得倒卖，必须配合合法取得的同版本完整原版游戏使用。问题反馈请提供Build、补丁版本、截图、位置、前后流程及错误日志。
