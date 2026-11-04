<p align="center">
  <img src="assets/hokucat.png" width="100" height="100" alt="Hokucat black cat and amber star">
</p>

<h1 align="center">Hokucat</h1>

<p align="center"><strong>A little life on your Mac desktop.</strong></p>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a> · <a href="docs/i18n/README.zh-TW.md">繁體中文</a> · <a href="docs/i18n/README.ja.md">日本語</a> · <a href="docs/i18n/README.ko.md">한국어</a> · <a href="docs/i18n/README.pt-BR.md">Português (Brasil)</a> · <a href="docs/i18n/README.es.md">Español</a> · <a href="docs/i18n/README.fr.md">Français</a> · <a href="docs/i18n/README.ar.md">العربية</a>
</p>

Browse your wallpaper library, preview a work, and adjust its available settings in one window. Apply it when it feels right. Hokucat brings animated scenes and playful characters to macOS, including a little black cat that follows your pointer and chases a star you can drag.

![Hokucat Wallpaper Dashboard with library, preview, and settings together](assets/hokucat-dashboard.jpg)

*Wallpaper Dashboard, captured in the 1.4.73 review build.*

[![Short Hokucat cat preview; click to watch the edited showcase](assets/hokucat-demo.gif)](assets/hokucat-demo.mp4)

[Watch the showcase video](assets/hokucat-demo.mp4) · [Create a wallpaper](docs/ai-wallpapers.md) · [FAQ](docs/faq.md)

*The video is an edited wallpaper showcase. Third-party PC works shown in the preview materials are for testing only; see [authors and original pages](docs/credits.md).*

## Try Hokucat

**1.4.74 is a preview release. The installer is pending distribution review and is not available for public download yet.** See the [release page](https://github.com/ar-gen-tin/hokucat/releases) for the current status and preview materials.

The current Mac build targets **macOS 13 or later**, on **Apple silicon and Intel**. If you already have a review build:

1. Open Hokucat from the menu bar and choose **Wallpaper Dashboard…**.
2. Select a wallpaper. Preview it and adjust the controls available for that work on the same page.
3. Click **Apply Wallpaper**. If you use more than one display, choose the destination first.

## Make the desktop yours

- **A library you can browse.** Find a wallpaper with search, arrange the collection manually, or sort by name.
- **Preview and settings together.** See the selected work alongside its controls. For supported videos, adjust the fit, speed, and horizontal flip before applying.
- **Simple library management.** Drag entries to reorder them, use a right-click menu for common actions, and remove imported wallpapers with confirmation. Your original source files stay where they are.
- **Mac interactions that feel at home.** Keep Hokucat in the menu bar, use familiar desktop controls, and play with the cat’s pointer tracking and draggable star. Available interactions vary by wallpaper.
- **Optional display-by-display choices.** Use a different wallpaper on each connected display; Hokucat remembers the choices.

The app interface is available in **English, Simplified Chinese, Traditional Chinese, Japanese, Korean, Brazilian Portuguese, Spanish, French, and Arabic**. Choose a language in Settings.

## Create a wallpaper with AI

Use Codex or Claude Code to make an original silent video loop, or bring a video you have permission to use. The [creation guide](docs/ai-wallpapers.md) includes a prompt and a runnable example that makes a package ready for **Wallpaper Dashboard → Import…**.

Package v1 supports **PNG/JPEG images and silent MP4/MOV/M4V videos**. AI helps create the media; Hokucat plays the imported files locally. General interactive Web or Windows Scene projects, live pointer or audio input, and live API or agent connections are outside this package format. Selected built-in or adapted wallpapers can have their own interactive features.

The procedural animation made by [`examples/make-wallpaper.py`](examples/make-wallpaper.py) is a self-contained example created for this repository. It is separate from the third-party PC wallpapers shown for testing.

## Questions, feedback, and credits

Read the [FAQ](docs/faq.md) for compatibility and import details, or [report an issue](https://github.com/ar-gen-tin/hokucat/issues) with your macOS version, Hokucat version, and steps to reproduce it. Documentation, translation, and example improvements are welcome—see [Contributing](CONTRIBUTING.md).

This repository contains the public documentation, showcase materials, and creation example. It does **not** contain the complete Mac application source. See the [changelog](CHANGELOG.md) for the documented preview changes.

Hokucat grew from [Grok Bot Wallpaper](https://github.com/Bodila51/grokbot-wallpaper) by **0xCodila (Bodila51)**. Third-party works remain credited to their creators; showing them in a test build does not grant permission to redistribute them. [Project lineage and asset credits](docs/credits.md)
