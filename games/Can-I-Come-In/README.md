# Can I Come In? 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/4969200/Can_I_Come_In/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4969200/ced187a5a2f19e9e690b8cd3d0f336382b2a1f3d/header.jpg?t=1787862205" alt="Can I Come In? 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：月见鸟**

## 发布信息

- **适用版本：** Steam AppID 4969200 的 Windows 版；包内未注明 BuildID（发布时公开 BuildID 24995059，仅作静态参考）
- **游戏引擎：** Unreal Engine
- **补丁技术：** Unreal PAK / IoStore 高优先级覆盖容器
- **Release 文件：** `Can-I-Come-In-Simplified-Chinese.7z`
- **文件大小：** 4,121,815 字节
- **SHA-256：** `EB23AAB6115905F9691BB6066B6FE9B29510B5FCB3E5877C85A8B597BFB71AEC`
- **压缩包文件数量：** 4
- **发布状态：** 已发布
- **下载地址：** [Can I Come In? 简体中文汉化](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/can-i-come-in-cn-20260902)

## 汉化内容

本补丁提供《Can I Come In?》的简体中文覆盖资源。外层压缩包包含一组 Unreal PAK / IoStore 补丁容器和使用说明；包内未附详细汉化范围清单，因此本页不对具体界面、剧情、字幕或图片的完成度作超出静态证据的承诺。

## 安装说明

1. 完全退出游戏。
2. 建议先备份 `CanIComeIn\NeighborsProject1\Content\Paks` 中可能被覆盖的同名文件。
3. 将 7Z 内的 `NeighborsProject1-Windows_P.pak`、`NeighborsProject1-Windows_P.ucas` 和 `NeighborsProject1-Windows_P.utoc` 解压到 Steam 游戏目录下的 `CanIComeIn\NeighborsProject1\Content\Paks`。
4. 如系统提示存在同名文件，请确认已完成备份后再覆盖。
5. 包内说明未要求选择特定语言；从 Steam 正常启动游戏。
6. 首次启动后请检查菜单、剧情文字和字幕是否正常显示。

## 卸载说明

从 `CanIComeIn\NeighborsProject1\Content\Paks` 删除上述三个 `_P` 补丁文件。若安装时覆盖了同名文件，请恢复安装前备份；必要时可通过 Steam 验证游戏文件完整性。

## 兼容性说明

- 面向 Steam AppID 4969200 的 Windows 版制作。
- 压缩包说明未记录明确的游戏版本或 BuildID；发布时公开分支 BuildID 24995059 仅作为静态基线，不代表已经完成运行兼容性验证。
- 包内未说明补丁基于英文版还是俄文版；纯英文原版的实际兼容性需用户手动验证。不要与其他覆盖同名 `_P` 文件的补丁混用。
- 游戏更新后若资源版本、IoStore 结构或挂载规则变化，可能导致汉化失效、显示异常或启动问题。
- 本补丁不能独立运行，必须配合合法取得的完整原版游戏使用。

## 静态校验

- 7Z 压缩包可正常列出并解包，共 4 个文件，第一层均为文件，无子目录。
- 压缩包大小为 4,121,815 字节，SHA-256 为 `EB23AAB6115905F9691BB6066B6FE9B29510B5FCB3E5877C85A8B597BFB71AEC`。
- `NeighborsProject1-Windows_P.pak`：73,773,383 字节，SHA-256 `42AA38506652EDF87A01A3BE833E87FB013F1EC87843A9D8BCA0EA0F2800C628`。
- `NeighborsProject1-Windows_P.ucas`：64 字节，SHA-256 `85F946CF2C8FFB7A6081D1C7D7EB95F2891C882342027B33A524B58174969044`。
- `NeighborsProject1-Windows_P.utoc`：202 字节，SHA-256 `0DCE1E30C38498366929008CAE13C5EF6C4C11DC140A709FAA34C2382E9352A2`。
- 未发现游戏 EXE、DLL、音频、视频、字体、日志、缓存、存档、源码、OBJ、PDB 或调试文件；未发现可独立运行的完整游戏。禁止文件检查限于外层压缩包清单和可读取文件，未使用 UnrealPak 完整枚举 PAK 内部资源。

## 反馈要求

反馈问题时请提供游戏版本或 BuildID、补丁版本、问题截图、出现位置、操作流程、相关日志和对应原文，以便定位。

## 验证声明

本次只完成压缩包结构、解包、文件读取和哈希静态校验，没有启动游戏。实际中文显示、完整剧情流程与当前版本兼容性仍需用户手动验证。

本汉化为非官方免费补丁，不得倒卖；必须配合合法取得的完整原版游戏使用。
