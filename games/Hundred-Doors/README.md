# Hundred Doors 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/3892240/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3892240/63116ee329c4d74adbf90953eabe2a71f1d072c6/header.jpg?t=1769433045" alt="Hundred Doors 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：Cokepoetry**

## 发布信息

- **适用版本：** Steam AppID 3892240，BuildID 21728869
- **游戏引擎：** Unreal Engine 4.27（Windows 64 位）
- **补丁技术：** 新增高优先级 PAK 覆盖，包含结构化 Blueprint/Kismet 修改、locres 本地化、图片文字和中文字体；附带 144 FPS 修改
- **Release 文件：** `Hundred Doors_简体中文覆盖包.zip`
- **文件大小：** 9,103,302 字节
- **SHA-256：** `431884A4B6BC5E60D896FFBCF48E85EC070B072F92631FFD8114952864BB357C`
- **压缩包文件数量：** 2
- **发布状态：** 待发布
- **下载地址：** [Hundred Doors 简体中文汉化 v8](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/hundred-doors-cn-20260827)

## 汉化内容

- 菜单、交互、物品、谜题、剧情和结局文本。
- 机场标牌等玩家可见的重要图片文字，保留原图标、箭头、数字和谜题关系。
- 中文字体及主菜单汉化署名。
- 补充灵烛、火柴、祭坛、理智提示、门选择、暂停菜单操作说明等 Blueprint/Kismet 硬编码文本。
- 补充 8 封道歉信、《维多利亚》艺术家陈述、L-33 放射科记录、《星夜》说明、西班牙语门谜题和七宗罪说明。
- 按用户需求将原版固定帧率从 60 FPS 调整为 144 FPS。

本页面只描述已写入当前构建并通过静态回读的内容，不代表所有低概率触发文本均已完成游戏内运行验证。

## 安装说明

1. 完全退出游戏。
2. 备份 `HundredDoors\Content\Paks` 中可能被覆盖的同名汉化文件。
3. 将覆盖包内全部文件复制到包含 `HundredDoors.exe` 的游戏根目录。
4. 系统询问时覆盖旧版 `HundredDoors_Chinese_P.pak`。
5. 无需安装 BepInEx、Unreal Editor 或其他汉化工具，也无需切换语言。
6. 首次启动保持游戏原生分辨率、全屏和输入设置。

## 卸载说明

删除 `HundredDoors\Content\Paks\HundredDoors_Chinese_P.pak` 即可卸载；也可通过 Steam 验证游戏文件完整性恢复原版状态。

## 兼容性说明

- 面向 Steam AppID 3892240、BuildID 21728869 制作。
- 可以直接安装到未装汉化工具的纯英文原版。
- 游戏更新后资源结构、BuildID 或挂载顺序变化可能导致补丁失效或崩溃。
- 144 FPS 实际效果仍受显示器刷新率、垂直同步和硬件性能影响；高帧率下物理及动画表现需用户手动确认。
- 补丁不修改分辨率、全屏模式、输入、音频、时间缩放、存档或注册表。

## 静态校验

- 覆盖包可正常读取，第一层为 `安装说明.txt` 与 `HundredDoors/`，不存在额外外层目录。
- PAK 使用 Unreal V8B、Zlib 压缩，共包含 129 个补丁文件。
- 回封后重新解包，129/129 个文件与构建树 SHA-256 一致。
- 二进制 FText 审计扫描 5,197 个 `.uexp`、533,892,182 字节；游戏主体识别 523 个 FText 实例。
- 本轮 36 个未归类实例已对账：15 个实例新增 locres、10 个实例由结构化 Blueprint 补丁处理、11 个实例为有理由的技术占位，未归类 missing 为 0。
- 最终 locres 含 390 个非空且不重复的 key；本轮 14 个新增目标全部在回读文件中找到。
- 压缩包未包含游戏主程序、原始主 PAK、日志、存档、缓存、源码、PDB 或调试文件。

## 反馈要求

请在 Issue 中提供游戏 BuildID、补丁版本、问题截图、出现位置、前后流程和可见原文。若发生崩溃，请附完整错误框与其中的资产路径。

## 验证声明

本版完成了容器解析、结构化编译、回封、解包、文本回读和哈希校验，没有启动游戏。实际显示、地图切换、低概率提示、文字布局和 144 FPS 表现仍需用户手动验证。

本汉化为非官方免费补丁，不得倒卖；必须配合合法取得的完整原版游戏使用。
