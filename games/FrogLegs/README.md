# FrogLegs 简体中文汉化

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/架构：Unreal Engine 5.3
- Release 文件：`FrogLegs_简体中文覆盖包.zip`
- 文件大小：5331047 字节
- ZIP SHA-256：`1E13F91B0423415B0F1743DF388D30C5131F480BA5027677A7034A54AD68F3F6`
- ZIP 文件数：4
- 发布审查状态：`release_ready`

> 该包采用新增覆盖文件或独立运行时组件，可在完成最终内容复核后作为 Release 附件发布。

## 安装说明

```text
FrogLegs 简体中文覆盖补丁
5050汉化组：Cokepoetry汉化

一、安装
1. 完全退出 FrogLegs。
2. 将覆盖包内的全部内容复制到 FrogLegs 游戏根目录。
3. 选择合并文件夹；本补丁只会新增 FPSCPP_Chinese_P.pak、FPSCPP_Chinese_P.utoc、FPSCPP_Chinese_P.ucas。
4. 从 Steam 或 FPSCPP.exe 正常启动游戏，保持游戏原生显示设置。

二、补丁结构
本补丁适用于 64 位 Unreal Engine 5.3 版本，采用新增 PAK/IoStore 覆盖容器，不需要安装 BepInEx、Unity 或 Unreal Editor，也不会覆盖原版 FPSCPP-Windows 容器。

补丁文件：
FPSCPP\Content\Paks\FPSCPP_Chinese_P.pak
FPSCPP\Content\Paks\FPSCPP_Chinese_P.utoc
FPSCPP\Content\Paks\FPSCPP_Chinese_P.ucas

三、本版汉化范围
1. 274 个 Inline FText 唯一键，在原始资源中命中 282 次；全部需要改写的静态菜单、设置、输入、章节与界面文字已写入中文。
2. 261 条 Blueprint/Kismet 剧情、对白和动态界面文本，已同步重映射内部跳转、Ubergraph 调用与外部事件入口。
3. 109 个默认 FString 唯一文本，实际写入 110 处；其中包括此前遗漏的地牢、住宅和公路开场三套对白数组，共补回 107 条剧情对白。
4. 202 条 Easy Game UI 本地化文本，以及 21 条公共 StringTable 选项文字。
5. 保留上一版已验证的中文字体、耳机提示图、章节画面和其他视觉资源。
6. 主菜单按钮显示“新游戏”；汉化署名显示在“Elliott Dahle 制作”下方并使用 16 号字，相对原 26 号入口字缩小约 38.5%。
7. 地牢骨骼谜语已按中文逻辑重译：慢炖肋排对应肋骨/胸腔，动脑子对应头骨，幽默与肱骨的双关对应肱骨；脚骨为干扰项。石像鬼谜语明确保留盾牌防守、长矛背后进攻的对应关系。

四、卸载
完全退出游戏后，仅删除以上 3 个 FPSCPP_Chinese_P 文件即可恢复原版。不要删除任何 FPSCPP-Windows 开头的原版文件。

五、兼容性
本补丁针对制作时检测到的 FrogLegs 64 位 Unreal Engine 5.3 构建（游戏界面版本 1.3，2025/11/11）。游戏更新后若出现英文恢复、资源不显示或流程异常，请先卸载补丁，并反馈游戏更新日期、问题截图以及 C:\Users\你的用户名\AppData\Local\FPSCPP\Saved 下的错误资料。

六、手动检查
1. 检查主菜单是否显示“新游戏、继续、设置、退出到桌面”，并确认小字号汉化署名没有遮挡。
2. 开始新游戏或读取存档，检查各章节对白、字幕、选项和场景切换。
3. 检查设置菜单、按键冲突提示、分辨率确认框、重置提示和 Easy Options 公共选项。
4. 检查中文字体、章节标题、输入提示、Boss UI、结局界面、耳机提示图和视觉资源。
5. Enter 键图例按用户要求保留按键标识。

按照用户要求，本次没有启动游戏、没有进行游戏内截图或运行测试，实际显示与流程由用户手动验证。
```

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。