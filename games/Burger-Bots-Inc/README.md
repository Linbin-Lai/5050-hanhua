# Burger Bots Inc 简体中文汉化

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/架构：Unity 2022.3.62f2 Mono
- Release 文件：`Burger Bots Inc_简体中文覆盖包.zip`
- 文件大小：28455405 字节
- ZIP SHA-256：`9522316ABDCB4B5CA36326C7E718DCB9BAB947A05DBD99A3432BD9FCE64A4A6E`
- ZIP 文件数：40
- 发布审查状态：`review_required_full_derived_asset`

> 当前 ZIP 含完整派生资源容器，上传前需复核是否包含大量原版资源；仓库中不得直接提交该文件。

## 安装说明

```text
Burger Bots Inc 简体中文覆盖补丁
汉化署名：5050汉化组：Cokepoetry汉化

安装：
1. 完全退出游戏和 Steam 的游戏启动进程。
2. 将本覆盖包内的全部文件复制到包含“Burger Bots Inc.exe”的游戏根目录。
3. 遇到提示时选择合并文件夹并覆盖同名汉化文件。
4. 从 Steam 或 Burger Bots Inc.exe 正常启动；保持游戏原生显示设置。

卸载：
1. 完全退出游戏。
2. 删除游戏根目录中的 winhttp.dll、doorstop_config.ini 和 .doorstop_version。
3. 删除 BepInEx\plugins\BurgerBotsChinese 文件夹。
4. 在 Steam 中验证游戏文件完整性，以恢复 Burger Bots Inc_Data\globalgamemanagers.assets 的英文启动画面原文件。
5. 若游戏目录中没有其他 BepInEx 插件，可一并删除 BepInEx 文件夹；如有其他插件，请保留该文件夹。

兼容性：
- 目标游戏：Burger Bots Inc 当前 Steam Windows 64 位版本。
- 引擎：Unity 2022.3.62f2，Mono 运行时。
- 框架：BepInEx 5.4.23.5 x64。
- 已内置与 Unity 2022 匹配的 ARIALUNI TMP 中文字体资产，不依赖系统临时生成 TMP 字体。
- 补丁完全离线运行，不需要安装 Unity。
- 本包包含运行所需的 BepInEx 文件，适用于尚未安装 BepInEx 的纯英文原版。
- 中文耳机/近距离语音提示属于 Unity 启动画面，覆盖包会替换同版本的 Burger Bots Inc_Data\globalgamemanagers.assets；该文件只修改 ProxyWarning 纹理。

注意：
- 本补丁不会主动修改分辨率、窗口模式、存档、时间缩放或游戏流程。
- 游戏更新后若 Steam 恢复了英文启动画面，需要重新安装与新版本兼容的汉化补丁，不要把旧版资源强行覆盖到未知新版本。
- 游戏内字体、贴图位置、联机流程与场景切换由用户手动验证。
- 首次运行后，日志位于 BepInEx\LogOutput.log；未命中文本可能记录在插件目录的 unknown-text.csv。
```

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。