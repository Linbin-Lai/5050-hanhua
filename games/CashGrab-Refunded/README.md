# CashGrab Refunded 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/3602720/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3602720/a8f24409032db54e302f6d24ab88d22335f4bfed/header.jpg?t=1762294159" alt="CashGrab Refunded 简体中文汉化 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/架构：Unity 6000.2.9f1 Mono
- Release 文件：`CashGrab Refunded_简体中文覆盖包.zip`
- 文件大小：7901515 字节
- ZIP SHA-256：`13870C95C98514EF0088B4D8D335CBD2CCD2815E6A108439E821D748DCDF4399`
- ZIP 文件数：71
- 发布审查状态：`published`
- 下载地址：[GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/cashgrab-refunded-cn-20260721)

> 已公开发布。附件不能独立运行，必须配合用户从 Steam 合法取得的对应完整原版游戏使用；具体完成范围和已知问题仍以本页安装说明为准。

## 安装说明

```text
CashGrab Refunded 简体中文覆盖补丁
5050汉化组：Cokepoetry汉化
补丁版本：1.3.6

一、安装
1. 完全退出游戏。
2. 将压缩包内全部文件直接复制到包含“PROJECT - REFUNDED.exe”的游戏根目录。
3. 保持游戏原生显示设置，从 Steam 或游戏主程序正常启动。

二、卸载
删除游戏根目录中的 winhttp.dll、doorstop_config.ini、.doorstop_version，以及 BepInEx 文件夹。
如果安装前已有其他 BepInEx 插件，请只删除 BepInEx\plugins\CashGrabRefundedChinese，不要删除其他用户文件。

三、兼容版本
游戏引擎：Unity 6000.2.9f1，64 位，Mono。
BepInEx：5.4.23.5，64 位 Mono 版。
当前兼容基线：
PROJECT - REFUNDED.exe SHA-256：BCA3602EC0AB3FA20BA055D8A84756A0A5B30EF10C03B790FDEAEBEDD2994854
Assembly-CSharp.dll SHA-256：09AF21329C8DB30B04F5A568A75ADCFC7AE58EB51763FC741CFF5F93D165617B
resources.assets SHA-256：A42E7EC56F55FDED001CA427F99927886111F3712A15565DC3D174FD33E0EC41

游戏更新后若上述哈希变化，请先停用补丁并等待适配，不要把旧补丁强行覆盖到新版本。

四、补丁内容
补丁离线运行，不修改存档、分辨率、全屏、帧率、时间缩放、输入设置或游戏流程。
程序文本使用精确文本表、受限动态模板与当前场景可见文本复核；匹配失败时保留英文原文。
中文字体使用随补丁附带的 Fusion Pixel Font 12px 简体中文版（SIL OFL 1.1），无需安装到 Windows。
玩家可见的教程图、操作牌、任务标识、海报、墙面文字和模型表面文字通过同尺寸纹理替换处理。

本版新增离线语音字幕：插件按 AudioClip 名称和播放时间显示底部居中的简体中文字幕，覆盖教程旁白、任务播报、角色对白和环境语音。字幕不会修改或替换原音频；纯笑声、尖叫、怪物叫声和机械音效不显示字幕。静音、停用、音量接近零或已经停止播放的声源不会触发字幕；距离衰减只用于多段语音的显示优先级，不再直接屏蔽字幕。

主菜单“开始游戏”下方会显示一次小号署名：
（5050汉化组：Cokepoetry汉化）

五、首次启动后请手动检查
1. 主菜单、署名和中文字体是否正常。
2. 设置、房间、目标、交互提示、物品名、ATM、服装属性和动态计数是否仍有英文。
3. 进入教程与任务后，确认英文语音出现时底部中文字幕能按台词切换，且不会遮挡关键操作提示。
4. 检查 21 点教程、复活教程、小妖电池插槽、拉杆、祭坛任务、托举同伴等操作图片。
5. 检查悬赏榜、投稿海报、宣传画、成就旗帜、禁止进入及其他墙面大字。
6. 检查是否存在缺字、方框、重叠、裁切、颜色异常或字幕时序偏差。

按照用户要求，本次没有启动游戏、没有进行游戏内截图或运行测试，实际显示与流程由用户手动验证。
```

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。