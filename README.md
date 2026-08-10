# 5050 汉化合集

本仓库用于整理和维护 **5050 汉化组**制作的游戏简体中文补丁、翻译文本、辅助脚本、校验信息及安装说明。

## 下载

可直接安装的汉化补丁统一通过仓库的 [**Releases** 页面](https://github.com/Linbin-Lai/5050-hanhua/releases)发布。仓库正文只保存说明、翻译表、构建脚本和校验信息，不把大型二进制补丁写入 Git 历史。

安装前请确认补丁适用于当前游戏版本，并完整阅读对应游戏目录中的说明。游戏更新后，旧版补丁可能失效或造成启动异常。

## 汉化项目

| 游戏 | 状态 | 补丁形式 | 项目说明 |
|---|---|---|---|
| Backrooms The Multiverse | 已发布 | Unreal IoStore 覆盖容器 | [查看](games/Backrooms-The-Multiverse/) |
| Bite Night: Dine or Die | 发布前复核 | Unity 静态资源 | [查看](games/Bite-Night-Dine-or-Die/) |
| Bite Night | 发布前复核 | Unity 静态资源 | [查看](games/Bite-Night/) |
| Burger Bots Inc | 发布前复核 | BepInEx + 资源补丁 | [查看](games/Burger-Bots-Inc/) |
| CashGrab Refunded | 已发布 | BepInEx 离线汉化 | [查看](games/CashGrab-Refunded/) |
| Endacopia | 已发布 | AGS 原生翻译与松散资源 | [查看](games/Endacopia/) |
| Fallen Leaf | 受限发布 | GameMaker 文本工具包 | [查看](games/Fallen-Leaf/) |
| FrogLegs | 已发布 | Unreal IoStore 覆盖容器 | [查看](games/FrogLegs/) |
| Funnel Runners | 已发布 | Unreal IoStore 覆盖容器 | [查看](games/Funnel-Runners/) |
| デテイケ -GetOut- | 已发布 | Unreal IoStore 覆盖容器 | [查看](games/GetOut/) |
| Hell of a Birthday | 发布前复核 | Unity 静态资源 | [查看](games/Hell-of-a-Birthday/) |
| Jeffrey Eggstein | 发布前复核 | Unity 静态资源 | [查看](games/Jeffrey-Eggstein/) |
| Mine of My Mind | 已发布 | BepInEx IL2CPP | [查看](games/Mine-of-My-Mind/) |
| Only Good Babysitters Go To Heaven | 发布前复核 | Unity 静态资源与字幕组件 | [查看](games/Only-Good-Babysitters-Go-To-Heaven/) |
| Pih 2 | 测试版 | Unreal PAK 本地化 | [查看](games/Pih-2/) |
| Strikers Club | 已发布 | Unreal IoStore 覆盖容器 | [查看](games/StrikersClub/) |
| UNBEATABLE | 已发布 | BepInEx 离线汉化 | [查看](games/UNBEATABLE/) |

“已发布”表示已有可安装版本，不代表所有低概率内容均经过运行验证。各项目的适用版本、已知问题和完成范围以独立说明为准。

## 仓库结构

```text
5050-hanhua/
|-- README.md
|-- CONTRIBUTING.md
|-- games/
|   |-- 游戏名称/
|   |   |-- README.md
|   |   |-- translations/
|   |   |-- scripts/
|   |   `-- checksums/
|-- shared-tools/
|-- docs/
`-- releases/
    `-- manifest.json
```

- `games/`：每款游戏的安装说明、兼容信息和公开源文件。
- `translations/`：可公开的中英文翻译表与术语表。
- `scripts/`：文本导入、导出、构建和静态校验脚本。
- `checksums/`：原版兼容基线及发布文件 SHA-256。
- `shared-tools/`：由本项目编写的通用辅助脚本。
- `releases/manifest.json`：全部发布包的文件名、大小和校验值。

## 问题反馈

请在 Issue 中提供游戏名称、游戏版本、补丁版本、问题截图、出现位置和操作流程。崩溃问题还应附带完整错误提示或日志。语音问题请补充说话人、场景、大致时间和能听清的英文原文。

## 版权与使用声明

游戏名称、程序、剧情、角色、美术、音频及其他原始资源的著作权归各自权利人所有。本项目是非官方、非商业的爱好者本地化项目，与游戏开发商、发行商及游戏平台无隶属或授权关系。

本仓库不提供游戏主程序、完整原始资源包、可替代正版游戏运行的文件，以及未经许可重新分发的字体、音频、视频或商业工具。使用本项目通常需要用户合法持有对应游戏。

未经明确许可，不得将本项目内容用于倒卖、付费代装、捆绑销售或其他商业用途。转载时请保留项目地址、适用版本、安装说明及汉化署名。

仓库内自行编写的脚本、翻译文本和游戏派生资源可能适用不同的使用条件。当前仓库不设置统一开源许可证；没有明确授权不代表可以任意复制、修改或商业使用。

## 汉化署名

**5050 汉化组：Cokepoetry 汉化**

## 免责声明

非官方汉化可能引起游戏无法启动、存档不兼容、联机校验失败或其他异常。安装前请备份重要文件，并严格核对适用版本。维护者不对因安装、混用、转载或自行修改补丁造成的数据损失承担责任。
