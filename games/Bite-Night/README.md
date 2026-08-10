# Bite Night 简体中文汉化

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/架构：Unity 2022.3.20f1 Mono
- Release 文件：`Bite Night_简体中文覆盖包.zip`
- 文件大小：64013790 字节
- ZIP SHA-256：`C1FD629A3E61A8A63D4E23DB530578BF55754D286CE3E8DDF1B439816CF59941`
- ZIP 文件数：5
- 发布审查状态：`review_required_full_derived_asset`

> 当前 ZIP 含完整派生资源容器，上传前需复核是否包含大量原版资源；仓库中不得直接提交该文件。

## 安装说明

```text
Bite Night 简体中文静态覆盖补丁
汉化署名：5050汉化组：Cokepoetry汉化

适用版本
Unity 2022.3.20f1、Windows 64 位 Mono 版。
本补丁按 Bite Night V0.06 当前本地文件构建。
补丁不使用 BepInEx，不要求预装任何汉化工具。
游戏更新后请勿继续使用旧补丁，应先恢复英文原版并重新构建。

安装
1. 完全退出游戏。
2. 打开包含“Bite Nite.exe”的目录。
3. 将本 ZIP 第一层的“Bite Nite_Data”和“安装说明.txt”直接复制到该目录。
4. 允许覆盖同名派生资源和 Assembly-CSharp.dll。
5. 正常启动游戏并保持游戏原生显示设置。

卸载
推荐在 Steam 中验证游戏文件完整性，恢复以下英文原版文件：
- Bite Nite_Data\level0
- Bite Nite_Data\resources.assets
- Bite Nite_Data\sharedassets0.assets
- Bite Nite_Data\Managed\Assembly-CSharp.dll

补丁内容
- 全量解析 11 个 DialogueEditor 对话对象，共 250 个对白与说话人字段。
- 结构化改写 Unity 场景文本和对话 JSON。
- 使用 Mono.Cecil 精确替换 Assembly-CSharp.dll 中的玩家可见硬编码字符串。
- 保留 RestartGame 等内部调用标识符，不改变游戏流程。
- 将 Noto Sans CJK SC 嵌入原 Font 资源，并配置 TMP 动态中文回退链。
- 静态替换开始、设置、退出、任务清单和卫生间指示牌纹理。
- 开始游戏按钮下方显示一次“5050汉化组：Cokepoetry汉化”。

静态校验
- 从最终 level0 重新提取全部 250 个对话字段，拉丁字母残留为 0。
- 4 个字体对象与字体源 SHA-256 一致，译文所需汉字静态缺字数为 0。
- 6 张替换纹理均已从最终资源重新解码；尺寸、格式和 mip 数量与原资源一致。
- Assembly-CSharp.dll 经 Mono.Cecil 回读，精确替换后映射源残留为 0。

已知风险
- 游戏内实际字号、换行、材质渲染和动态生成字形仍需手动运行确认。
- “YEAH!”短语音没有足够安全的原生字幕绑定入口，本版暂不注入该字幕，以免改动播放流程。

按照用户要求，本次没有启动游戏、没有进行游戏内截图或运行测试，
实际显示与流程由用户手动验证。
```

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。