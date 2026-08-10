# Only Good Babysitters Go To Heaven 简体中文汉化

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/架构：Unity 2022.3.20f1 Mono
- Release 文件：`Only Good Babysitters Go To Heaven_简体中文覆盖包.zip`
- 文件大小：25987810 字节
- ZIP SHA-256：`C01390110015150CD9D9C2E307852F2BA332CB309E688E8C3CB876F4E4ACCD78`
- ZIP 文件数：7
- 发布审查状态：`review_required_full_derived_asset`

> 当前 ZIP 含完整派生资源容器，上传前需复核是否包含大量原版资源；仓库中不得直接提交该文件。

## 安装说明

```text
《Only Good Babysitters Go To Heaven》简体中文汉化

安装：
1. 完全退出游戏。
2. 将压缩包内全部内容复制到游戏 EXE 所在目录，选择覆盖。
3. 从 Steam 或游戏主程序正常启动，保持游戏原生显示设置。

卸载：
在 Steam 中验证游戏文件完整性，并删除：
Only Good Babysitters Go To Heaven_Data\Managed\OnlyGoodBabysittersChinese.dll
Only Good Babysitters Go To Heaven_Data\Managed\audio_subtitles.tsv

兼容版本：Unity 2022.3.20f1、Windows 64 位 Mono 版。
原版 Assembly-CSharp.dll SHA-256：F3874E226EEAA58CC86FDE8580FCEBFD7B926BCF594A8894F911007C00860D9C
游戏更新后若该哈希变化，请勿继续使用本包，应基于新版本重新构建。

实现说明：
本汉化直接修改 Unity 静态资源及 Assembly-CSharp.dll，不使用 BepInEx、Doorstop、Harmony 或 XUnity。
黑框字幕只补充没有现成对话框的英语语音；已绑定原生对话框的主对话音频从字幕表排除，不会重复显示对话框文字。ConversationEventInfo 中实际没有文字框的短语音已逐条复核并补入字幕。录制婴儿对白只响应 Timeline 的真实片段播放，不响应普通静默或循环 AudioSource，避免无语音时误弹字幕。
字幕按真实 AudioSource 播放状态显示，只显示中文内容，不显示角色名，不使用角色颜色。长语音按实际播放进度逐句切换，不会一次显示整段；并发语音最多同时显示三条，各自停止后独立清除。

首次启动请重点检查主菜单署名、中文字体、对话与选项、环境语音字幕、图片文字和长文本布局。实际显示与流程仍需用户手动验证。

汉化署名：5050汉化组：Cokepoetry汉化
```

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。