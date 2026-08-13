# 鳴蟇村（NARIBIKIMURA）简体中文汉化

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/容器：Unreal Engine IoStore（PAK / UTOC / UCAS）
- Release 文件：`NARIBIKIMURA_简体中文覆盖包.zip`
- 文件大小：1201934 字节
- ZIP SHA-256：`5F281B84C13FE4774E5B3D0DFF7AF4AE9EA6CC7CD94DA5D972FD3177859523FD`
- ZIP 文件数：4
- 发布审查状态：`published`
- 下载地址：[GitHub Release](https://github.com/Linbin-Lai/5050-hanhua/releases/tag/naribikimura-cn-20260813)

> 附件不能独立运行，必须配合用户合法取得的完整原版游戏使用。本版本除中文汉化外，还将帧率上限调整为 120 FPS。

## 安装说明

```text
《鳴蟇村》简体中文覆盖包 v3（120 FPS）

包含：完整中文、Steam 简体中文首次启动自动进入中文分支、主菜单底部文字水印、120 FPS 上限。

帧率修改：配置默认值、游戏实例初始化/载入值、系统更新函数共 5 处由 60.0 改为 120.0。
若硬件性能不足，实际帧率仍会低于 120；垂直同步或显示器刷新率也可能限制实际帧率。

安装：
复制三个 NARIBIKIMURA_Chinese_P 文件到 NARIBIKIMURA\Content\Paks。

卸载：
关闭游戏后删除这三个文件。
```

## 静态校验

- ZIP 可正常读取，包含匹配的 `.pak`、`.utoc` 和 `.ucas` 三件套。
- 四个包内文件均已完整回读并计算 SHA-256，未发现解压错误。
- 未包含游戏主程序、原始主容器、日志、缓存或调试文件。
- 压缩包内额外包含一层 `NARIBIKIMURA_简体中文覆盖包` 文件夹；安装时应进入该文件夹后复制三个补丁文件。

## 反馈要求

反馈时请提供游戏版本、补丁 SHA-256、问题截图、所在位置和前后流程。

## 验证声明

本次仅完成静态解析、回读、哈希和文件结构检查；没有启动游戏，实际中文显示、120 FPS 修改和流程由用户手动验证。
