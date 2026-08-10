# Pih 2 简体中文汉化

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/架构：Unreal Engine 5.3
- Release 文件：`Pih 2_简体中文覆盖包.zip`
- 文件大小：406458 字节
- ZIP SHA-256：`9786F54D82546A89E64F2F704AF23ECAE793194C288694869DE6339B6D3B06C1`
- ZIP 文件数：2
- 发布审查状态：`published`
- 下载地址：[GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/pih-2-cn-20260806)

> 已公开发布。附件不能独立运行，必须配合用户从 Steam 合法取得的对应完整原版游戏使用；具体完成范围和已知问题仍以本页安装说明为准。

## 安装说明

```text
Pih 2 简体中文汉化补丁（5050汉化组：Cokepoetry汉化）
==================================================

【适用版本】
游戏引擎：Unreal Engine 5.3（++UE5+Release-5.3-CL-29314046），Win64 Shipping
原版容器：Pih2\Content\Paks\Pih2-Windows.pak
  大小   ：5,151,821,707 字节
  SHA-256：a2103b6c0d35672a9330bdf926a3b029e1da5960650686847714c540182eeca1
若你的 Pih2-Windows.pak 与上述大小/哈希不一致，说明游戏已更新，请勿直接使用本补丁。

【安装】
1. 完全退出游戏与 Steam 的游戏进程。
2. 找到包含 Pih2.exe 的目录，默认是：
   ...\steamapps\common\Pih 2\Windows\
3. 把本压缩包第一层的 Pih2 文件夹直接解压/复制进该目录，
   最终得到：
   ...\Pih 2\Windows\Pih2\Content\Paks\Pih2_Chinese_P.pak
4. 本补丁只新增一个文件，不覆盖、不删除任何原版文件。

【卸载】
删除 Pih2\Content\Paks\Pih2_Chinese_P.pak 即可完全还原为英文原版。
无需验证文件完整性，无需重装。

【本补丁做了什么】
- 以 Unreal 原生本地化机制（Content\Localization\Game 下的 Game.locres）
  为全部已提取的 FText 条目提供简体中文显示文本。
- 不修改任何原始 .uasset / .uexp / .pak，不注入 DLL，不使用 BepInEx /
  Doorstop / Harmony / 自动翻译器，不改动分辨率、窗口模式、帧率与输入设置。

【已汉化范围】
- 暂停菜单、设置菜单（画面/音频/操作/按键绑定）、难度选择
- HUD：得分、倍率、弹药、收集进度、免疫提示
- 结算奖杯界面：本次得分 / 最高分 / 季 / 关卡
- 武器、弹药、配件名称与类型枚举
- 伤害数字（暴击、护盾破碎、火焰、电击、酸蚀、冰冻等）
- 关卡内交互与操作提示（热气球、收集、教学房间说明等）
- Boss 名称（大肚培根轰天猪 鲍里斯）

- 主菜单气球贴图（DXT5 2000x2000）已重绘为中文：
  开始游戏 / 选择关卡 / BOSS关卡 / 退出游戏 / 返回 /
  赛季 1-4 / 最终之舞 / PIH 3 快来了？
  汉化署名位于「开始游戏」气球下方。

【视觉文字全量扫描结果】
- 枚举贴图资产 1,981 个 / 贴图对象 5,645 个
- 按通道名排除非颜色贴图（法线/ORM/粗糙度/AO/遮罩/高度）949 个
- 颜色贴图 1,032 个全部执行 OCR + 分批静态联系表人工复核
- 除已汉化的 11 张主菜单贴图外，未发现任何玩家可见英文贴图
- 保留原文的可见文字仅为品牌 Logo（Unreal Engine / Ultra Dynamic Sky /
  Ultra Dynamic Weather / FPS Animation Blueprint 水印），属 P3 装饰级豁免

【本版本尚未包含（重要）】
- 蓝图字节码（Kismet EX_StringConst）中的 36 个玩家可见字符串实例仍为英文，
  例如：Pick Up {Name} / Pickup {Name} / Get in/out / Headshot! / Points! /
  Hogpocalypse / Hawg Wild / Feral Hawg / Hawgmaster / Hawgtastic /
  The Underhawg / Frank The Hawgback Pihslinger / Ribert The Pitmaster /
  Sifu Sausage / SIGHTS / MUZZLE / MAGAZINE / STOCK / UNDERBARREL /
  Navigate Menu / Field of View / Mouse Sensitivity / Aiming Sensitivity /
  DROWN / NEW BEST! / Unequip 等。
  这些是 ANSI 定长常量，改成中文必然改变字节长度，需要完整的 Kismet
  反汇编/汇编与跳转地址重建才能安全替换；为避免产出可能崩溃的资产，
  本版本按原文保留。
- 英文语音/视频的中文字幕未制作（按用户要求本次不做）。

【首次启动注意】
- 直接用 Steam 或 Pih2.exe 正常启动即可，保持游戏原生显示设置。
- 中文字形由引擎自带 DroidSansFallback 回退字体提供，无需另外安装字体。
- 若某处仍显示英文，请截图并附上所在界面与前后流程反馈。

【说明】
按照用户要求，本次没有启动游戏、没有进行游戏内截图或运行测试，
实际显示与流程由用户手动验证。
```

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。