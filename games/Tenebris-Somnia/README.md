# Tenebris Somnia 简体中文汉化

<!-- game-cover:start -->
<p align="center">
  <a href="https://store.steampowered.com/app/2121510/">
    <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2121510/61f3fb4ddb5387876aa498f621386e1d4442c219/header.jpg?t=1792175122" alt="Tenebris Somnia 游戏封面" width="460">
  </a>
</p>
<!-- game-cover:end -->

**汉化作者：5050汉化组：Cokepoetry汉化**

## 发布信息

- 游戏：Tenebris Somnia（Steam AppID 2121510；开发商 Andrés Borghi、Saibot Studios；发行商 New Blood Interactive）
- 适用版本：按 2026-10-17 的本地英文资源制作；Steam BuildID 未记录，后续游戏版本未验证
- 引擎与补丁技术：Unreal Engine；PAK V11 新增覆盖容器，不替换原版 PAK
- 补丁版本：2026-10-17 首发
- Release 附件：`Tenebris_Somnia_CN_20261017.zip`（原始包名为 `Tenebris_Somnia_简体中文覆盖包.zip`，两者内容相同）
- 文件大小：774,566 字节
- SHA-256：`1E4EEC7A71AD3DA4ACA4C257A226CC3DEB0BAFB7A0169E967EBA9639966C54D7`
- ZIP 条目：4（目录 1、文件 3）
- 发布状态：已发布；静态校验完成，完整游戏流程仍待玩家验证
- 发布页面：[Tenebris Somnia 简体中文汉化](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/tenebris-somnia-cn-20261017)

## 汉化内容

覆盖包包含 1,824 条本地化文本及中文显示所需的字体资源，覆盖已定位的菜单、叙事、书页、物品和谜题文本，以及游戏现有字幕通道中的相关条目。主菜单“开始游戏”下方带有汉化署名。炼金术语统一采用“英文原词（中文译名）”，便于与谜题线索核对。原游戏图片和视频画面未改动；画面内可能仍有英文。过场字幕的实际显示时序尚未全流程实测。

## 安装说明

1. 完全退出游戏，备份现有的 `TenebrisSomnia\Content\Paks\TenebrisSomnia_Chinese_P.pak`（若存在）。
2. 将 ZIP 中的 `TenebrisSomnia` 文件夹解压到含 `TenebrisSomnia.exe` 的游戏根目录，使目录合并；如果系统提示同名汉化补丁，选择覆盖。
3. 正常启动游戏。本补丁直接覆盖英文资源，不需要选择额外语言。

压缩包中的 `安装说明.txt` 和 `SHA256校验.txt` 可留作参考。不要把 ZIP 中的 PAK 解压到游戏根目录以外的其他 `Paks` 文件夹。

## 卸载与兼容性

退出游戏后删除 `TenebrisSomnia\Content\Paks\TenebrisSomnia_Chinese_P.pak`，或恢复安装前备份的同名文件。原版 PAK 不会被替换。补丁按制作时的英文资源构建，未获得 Steam BuildID；游戏更新后可能不兼容，请先核对。补丁不能独立运行，必须配合合法取得的完整原版游戏使用。

## 静态校验与授权提醒

已读取 ZIP 全部 4 个条目，核对内层 PAK、安装说明与校验文件；内层 PAK 拆包得到 3 个资源文件，并与构建文件一致。1824 条本地化文本已通过静态重导出检查。未发现游戏主程序、独立启动器、存档、日志、源码、PDB 或独立音视频。

PAK 内含从原游戏资源修改的字体数据，其中 Arial 字体带有 Monotype 的授权声明；字体及原作版权归各权利人。本项目未取得字体的单独再分发授权，公开附件可能面临权利人投诉或下架风险。本汉化为非官方免费补丁，不得倒卖；如有权利问题，请通过仓库联系维护者。

## 反馈要求

反馈时请附游戏版本或 BuildID、补丁发布日期、截图、所在章节或界面、触发流程以及英文原文。崩溃问题请附错误信息或日志；谜题问题请注明相应书页、道具和线索。

## 验证声明

制作阶段完成了压缩包、资源结构、文本回读与哈希等离线检查，并收到主菜单的玩家截图确认；其他新增术语的排版、过场字幕时序和完整游戏流程尚需玩家手动验证。
