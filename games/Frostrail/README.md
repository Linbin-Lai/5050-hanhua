# Frostrail 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/3517740/Frostrail/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3517740/24567900b45648a5b962cabf9898258b1c1d50ba/header.jpg?t=1788856599" alt="Frostrail 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：月见鸟**

## 发布信息

- **适用版本：** 包内说明指向 Windows 版 `Frostrail Playtest`；未注明 BuildID
- **游戏引擎：** Unreal Engine
- **补丁技术：** PAK / IoStore 覆盖容器
- **Release 文件：** `Frostrail-Simplified-Chinese-Yuejianniao.7z`
- **文件大小：** 1,843,754 字节
- **SHA-256：** `75EDC6CA65A7E5C8A8F6AACC6EC9791AC8B96B918E4ECA5836F7B3A81B572E23`
- **压缩包文件数量：** 4
- **发布状态：** 已发布
- **下载地址：** [Frostrail 简体中文汉化（月见鸟）](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/frostrail-cn-20260916)

## 汉化内容

本补丁提供《Frostrail》Playtest 版本的简体中文覆盖资源。压缩包包含 `zh.pak`、`zh.ucas`、`zh.utoc` 和包内使用说明。包内没有提供逐项汉化范围，因此本页不对界面、剧情、字幕或图片的具体完成度作超出静态证据的承诺。

## 安装说明

1. 完全退出游戏。
2. 将压缩包内四个文件解压到：
   `Steam\steamapps\common\Frostrail Playtest\Frostrail\Content\Paks`
3. 保持 `zh.pak`、`zh.ucas` 和 `zh.utoc` 成套存在，不要只安装其中一个容器。
4. 从 Steam 正常启动游戏并手动检查中文显示。

## 卸载说明

从上述 `Paks` 目录删除本补丁添加的 `zh.pak`、`zh.ucas`、`zh.utoc` 和使用说明。不要删除游戏原有容器。

## 兼容性说明

- 包内说明明确使用 `Frostrail Playtest` 路径；不能据此保证兼容未来正式版或其他测试分支。
- Steam 商店 AppID 3517740 仅作为游戏页面参考；压缩包未记录 Playtest AppID、BuildID 或资源基线哈希。
- 游戏更新后若 Unreal 资源版本、IoStore 结构或挂载规则变化，补丁可能失效或造成启动异常。
- 本补丁不能独立运行，必须配合合法取得的完整原版游戏使用。

## 静态校验

- 7Z 压缩包可正常列出并解包，共 4 个文件；未发现游戏 EXE、DLL、存档、日志或缓存。
- `zh.pak`：62,735,897 字节，SHA-256 `FBA05EEFA6D855D38958B592D940D80F770C163FD9E29E2FB7DD37441C5198EB`。
- `zh.ucas`：64 字节，SHA-256 `85F946CF2C8FFB7A6081D1C7D7EB95F2891C882342027B33A524B58174969044`。
- `zh.utoc`：202 字节，SHA-256 `0DCE1E30C38498366929008CAE13C5EF6C4C11DC140A709FAA34C2382E9352A2`。
- `使用说明.txt`：82 字节，SHA-256 `EBF8BDEDB68F90733DBD00365FB13893ECC5974C6E43141041B46EB0D7981B6B`。
- 未使用 UnrealPak/IoStore 工具完整枚举 `zh.pak` 内部资产，本页只报告外层归档与容器文件静态结果。

## 反馈要求

反馈问题时请提供 Playtest 版本或 BuildID、问题截图、出现位置、操作流程、完整错误信息及补丁 SHA-256。

## 验证声明

本次只完成压缩包结构、解包、文件读取和哈希静态校验，没有启动游戏。实际中文显示、完整流程与当前 Playtest 版本兼容性仍需用户手动验证。

本汉化为非官方免费补丁，不得倒卖；转载时请保留“月见鸟汉化”署名，并配合合法取得的完整原版游戏使用。
