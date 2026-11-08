# Changelog

These entries describe verified changes in the preview builds. See the [project overview](README.md) for demos and the [FAQ](docs/faq.md) for installation details.

## 1.4.80 — Last Horizon

[Download the DMG](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.80/Hokucat-1.4.80.dmg) · [SHA-256 checksums](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.80/SHA256SUMS.txt)

- Add Last Horizon: click to open or close the eyes, cycling through blue, amber, and feline irises on each opening.
- Deliver 4K output using the 8K still artwork and an adapted 1440p source animation; the moving source is upscaled, not native 4K.
- Return to still frames between eye movements and release the video player while idle.
- Retain contributor credits, original source links, and both upstream MIT license texts. See [Last Horizon credits](docs/credits.md#last-horizon).
- Verified all 19 bundled Last Horizon files (16 media SHA-256 values plus source metadata and license copies) and the 13-entry launch manifest. Passed 65 Python tests, Creator Kit checks, and native offscreen integration checks. DMG mounting confirmed the packaged app matches the tested app; the app and DMG passed Developer ID signature verification.
- Developer ID–signed preview, not notarized. Long-duration observation, physical sleep/wake, and Intel runtime tests were not performed for this build.

## 1.4.77 — Cinderella memory update

[Download the DMG](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.77/Hokucat-1.4.77.dmg) · [SHA-256 checksums](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.77/SHA256SUMS.txt)

- Release hidden Cinderella scene textures after transitions, and restore them when needed. Image resolution, materials, and animation settings are preserved.
- In one local A/B test against 1.4.76 at the same display size, the warmed-up lobby observation median for the app and its attributed WebKit processes fell from 745.53 MiB to 673.53 MiB (72.00 MiB, about 9.7%). This is a short, scene-specific measurement, not a guarantee for every wallpaper or Mac.
- Passed 26 exact before/after frame comparisons, interaction and graphics-recovery checks, 65 Python tests, and release smoke checks. About eight minutes of installed dual-display observation showed one app instance, two wallpaper windows, and no newly logged faults in the monitored categories.
- Remove build-machine paths from debug symbols in the distributed executable.
- Developer ID–signed preview, not notarized. Long-duration, cross-device, Intel runtime, physical sleep/wake, and display hot-plug tests were not performed for this build.

## 1.4.74 — Signed preview

[Download the DMG](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/Hokucat-1.4.74.dmg) · [SHA-256 checksums](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/SHA256SUMS.txt)

- Developer ID–signed preview for macOS 13 or later, on Apple silicon and Intel. Apple notarization is not complete, so macOS may block the app when first opened.

- Star Citizen uses a still cover while browsing the review library, avoiding unnecessary simultaneous video playback. Selecting a cover does not need to start another video player.

## 1.4.73 — Review build

- Reworked the Hokucat cat scene, retaining pointer tracking, the draggable star, and its star trail.

## 简体中文

以上仅记录已核验的预览版变化，安装说明见[常见问题](docs/faq.md#简体中文)。

- **1.4.80：** [下载已签名预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.80/Hokucat-1.4.80.dmg)。新增 Last Horizon，点击开合双眼，每次睁眼依次切换蓝瞳、琥珀瞳与猫瞳。以 8K 静态原画和经过适配的 1440p 原动画提供 4K 输出，动态底片经放大处理，并非原生 4K。静止时显示静态帧并释放视频播放器。保留贡献者署名、原始来源及两份上游 MIT 许可，详见[Last Horizon 署名](docs/credits.md#last-horizon)。已核对 19 份 Last Horizon 文件（16 份媒体的 SHA-256，以及来源记录与许可副本）和 13 项发行清单；通过 65 项 Python 测试、Creator Kit 与原生离屏集成检查，DMG 挂载确认包内应用与受测应用一致，应用和 DMG 的 Developer ID 签名验证通过。已签名、未公证；本版未补做长时观察、整机睡眠唤醒和 Intel 实机运行测试。

- **1.4.77：** [下载已签名预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.77/Hokucat-1.4.77.dmg)。优化 Cinderella 隐藏场景的纹理释放与恢复，保留画质和互动。同尺寸本机 A/B 短时测试中，预热后大厅观察段的应用与关联 WebKit 物理内存中位数从 745.53 MiB 降至 673.53 MiB，减少约 9.7%。通过 26 组画面逐像素对照、互动与图形恢复检查、65 项 Python 测试和发布烟测；约八分钟双屏观察保持单实例、两个壁纸窗口，监测范围内未记录新故障。发行文件已清除构建目录信息。已签名、未公证；本版未补做长时、跨设备、Intel 实机、整机睡眠唤醒和外屏拔插测试。

- **1.4.74：** [下载已签名预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/Hokucat-1.4.74.dmg) · [SHA-256 校验值](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/SHA256SUMS.txt)。支持 macOS 13 或更新版本以及 Apple 芯片和 Intel Mac，已使用 Developer ID 签名。Apple 公证尚未完成，macOS 可能阻止首次打开。浏览测试壁纸库中的 Star Citizen 时使用静态封面，避免仅选中封面就多开一路视频播放。
- **1.4.73：** 重做 Hokucat 小黑猫场景，保留鼠标追视、星星拖动和碎星轨迹互动。
