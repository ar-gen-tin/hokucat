# Frequently asked questions

[English README](../README.md) · [简体中文](#简体中文)

## Can I download Hokucat now?

The 1.4.74 preview has showcase materials, but its installer is still pending distribution review. No public installer is available yet. Check the [release page](https://github.com/ar-gen-tin/hokucat/releases) for availability. The current Mac build targets macOS 13 or later on Apple silicon and Intel.

## How do I change a wallpaper?

Open **Wallpaper Dashboard…** from the menu bar, select a wallpaper, preview it and adjust its available settings, then click **Apply Wallpaper**. With multiple displays, select the destination first. Browsing another wallpaper does not apply it automatically.

![Video controls beside the library in the review build](../assets/hokucat-inline-settings.jpg)

*Actual app screenshot. Star Citizen and the other third-party works shown are for testing only. [Credits and original pages](credits.md)*

## Can I sort or remove wallpapers?

You can search, sort by name, or use manual order and drag entries into place. Some default entries stay pinned. Supported entries can be removed through the confirmation dialog; the original files you imported stay unchanged. If a removed wallpaper is in use, the dialog names the affected displays and the app switches them to a built-in wallpaper.

## Does it run every Wallpaper Engine wallpaper?

No. Compatibility depends on the work and its format. Selected PC Web wallpapers have specific adaptations; some Windows Scene works are shown as recordings or catalogue entries. A recording does not reproduce the original live effects or settings. The dashboard labels these differences. The current review selection is not a promise that all Workshop content can run or be imported.

Third-party PC works shown in review materials are **for testing only**, belong to their original creators, and are linked in [Credits](credits.md). Attribution and a Workshop subscription do not establish permission to redistribute a work.

## What can I create and import?

Package v1 accepts PNG/JPEG images and silent MP4/MOV/M4V videos, with a preview, fallback image, and source/usage information in a package folder. Select the whole folder with **Import…**. The [creation guide](ai-wallpapers.md) and [`make-wallpaper.py`](../examples/make-wallpaper.py) help prepare one.

AI can help write a rendering script or make the source media. Imported v1 packages play locally and do not require an AI connection. They do not support general interactive Web or Windows Scene projects, live pointer/audio input, or live API/agent connections. A built-in interactive wallpaper can have capabilities that this import format does not.

## Can I use different wallpapers on different displays?

Yes. Choose the display in the dashboard before applying a wallpaper. The app stores each display’s choice separately.

## Can I change the interface language?

Yes, in **Settings**. Available languages are English, Simplified Chinese, Traditional Chinese, Japanese, Korean, Brazilian Portuguese, Spanish, French, and Arabic.

## Is the full app source in this repository?

No. This repository contains public documentation, showcase materials, and the creation example. It is not a complete source checkout of the Mac app. The app’s lineage is documented in [Credits](credits.md).

## How should I report a problem?

Open an [issue](https://github.com/ar-gen-tin/hokucat/issues) with the Hokucat and macOS versions, the wallpaper title or original page, what you expected, and the steps that produced the problem. For display issues, include the number of displays and their resolutions. A cropped screenshot or short recording can help; remove private desktop content first. See [Contributing](../CONTRIBUTING.md) for documentation, translation, and example changes.

## 简体中文

### 现在能下载吗？

1.4.74 预览版提供演示材料，安装包仍待分发审核，暂未开放公开下载。请以 [GitHub 发布页](https://github.com/ar-gen-tin/hokucat/releases)为准。当前 Mac 构建面向 macOS 13 或更新版本，包含 Apple 芯片和 Intel 版本。

### 怎么换壁纸、排序和移除？

从菜单栏打开「壁纸面板」，选中作品，在同页预览和调整设置，点击「应用壁纸」才会切换。多显示器用户先选择屏幕。壁纸库支持搜索、按名称排序和手动拖动排序，部分默认作品固定在前面。可移除的条目会先弹出确认；导入前的原始文件不会被改动。若作品正在使用，确认窗口会列出受影响的屏幕，移除后切换到内置壁纸。

### 所有 Wallpaper Engine 壁纸都能用吗？

不能。兼容性取决于作品及格式。部分 PC Web 作品经过单独适配，部分 Windows Scene 作品以录屏或目录预览展示；录屏不会保留原作的实时特效和设置，界面会标明区别。当前测试作品不能代表全部创意工坊内容都能运行或导入。

预览材料中的第三方 PC 作品**仅供测试使用**，归原作者所有，作者与原作链接见[署名页](credits.md)。署名或订阅创意工坊作品不等于获得再分发许可。

### AI 创作和导入支持什么？

作品包 v1 支持 PNG/JPEG 静态图和静音 MP4/MOV/M4V 视频，需带预览图、回退图及素材来源和使用信息。在「导入…」中选中整个作品包文件夹。[创作指南](ai-wallpapers.md#中文快速开始)和[公开示例脚本](../examples/make-wallpaper.py)可帮助生成。

AI 参与脚本或素材创作，导入后的 v1 作品在本机播放，不需要连接 AI。此格式暂不支持通用交互式 Web、Windows Scene 工程、实时鼠标或音频输入，以及实时 API 或 Agent 连接。内置互动壁纸的能力可能超出此导入格式。

### 支持多显示器和中文吗？

支持。每块显示器可单独选择壁纸；「设置」提供英语、简体中文、繁体中文、日语、韩语、巴西葡萄牙语、西班牙语、法语和阿拉伯语。

### 完整应用已经开源了吗？

本仓库公开产品说明、演示材料和创作示例，未包含完整 Mac 应用源代码。项目来源见[署名页](credits.md)。

### 怎么反馈问题？

在 [Issues](https://github.com/ar-gen-tin/hokucat/issues) 提供 Hokucat 和 macOS 版本、壁纸名称或原作链接、预期效果和复现步骤。显示问题请附屏幕数量与分辨率；截图或录屏先避开私人内容。文档、翻译和示例贡献见[贡献说明](../CONTRIBUTING.md)。
