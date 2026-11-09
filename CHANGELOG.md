# Changelog

These entries describe verified changes in the preview builds. See the [project overview](README.md) for demos and the [FAQ](docs/faq.md) for installation details.

## 1.4.87 — Characters, Glass Clock, and supplements

[Download the DMG](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg) · [SHA-256 checksums](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/SHA256SUMS.txt)

- Consolidate Grok White, Grok Black, Muse, and Clawd into one **Characters** library entry, with inline character selection and native black/white appearance switching.
- Keep **Hokucat** separate, with its own manual color choice or automatic color mode.
- Add native **Glass Clock** with controls for time zone, size, second hand, and background.
- Add blister and frosted containers for the supplement wallpaper; correct undo and preview-setting behavior.
- Remove Dots, SpongeBob, NIKKE2B, and NIKKE4K01 from the default library. **NIKKE Cinderella remains.** Historical showcase materials retain their original credits.
- Version **1.4.87 / build 97** is a Developer ID–signed preview, not notarized. It is built for macOS 13 or later on Apple silicon and Intel; Intel hardware runtime is unverified. This release does not establish full PC wallpaper compatibility or sustained runtime, physical sleep/wake, and display hot-plug coverage.

## 1.4.81 — White cat edge repair

Archived preview · Downloads withdrawn. [Download the current 1.4.87 preview](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg).

- Restore the white cat’s soft fur silhouette around the ears, forehead, and cheeks by replacing the polygon cut-out with the original fur alpha, prepared once when the portrait loads.
- Preserve the closed-face blink, eye tracking, and shared portrait textures across displays.
- In a local 60-second offscreen comparison at 1920 × 1080, the median physical memory footprint with two active white-cat views fell from 62.36 MiB to 50.50 MiB, about 19%. This measures the isolated renderer process; it does not measure physical dual-display GPU/WindowServer load or long-run behavior.
- Passed a regression that fails on the old hard edge and passes on the repaired 4K render, day/night switching and shared-texture release checks, 65 Python tests, Creator Kit checks, and native offscreen integration. The white-cat repair was also visually checked in a native window on this Mac.
- Keep the same 13-entry library, including Last Horizon, with the existing credits and testing labels.
- Developer ID–signed preview, not notarized. Long-duration, Intel hardware, sleep/wake, and display hot-plug tests were not repeated for this build.

## 1.4.80 — Last Horizon

Archived preview · Downloads withdrawn. [Download the current 1.4.87 preview](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg).

- Add Last Horizon: click to open or close the eyes, cycling through blue, amber, and feline irises on each opening.
- Deliver 4K output using the 8K still artwork and an adapted 1440p source animation; the moving source is upscaled, not native 4K.
- Return to still frames between eye movements and release the video player while idle.
- Retain contributor credits, original source links, and both upstream MIT license texts. See [Last Horizon credits](docs/credits.md#last-horizon).
- Verified all 19 bundled Last Horizon files (16 media SHA-256 values plus source metadata and license copies) and the 13-entry launch manifest. Passed 65 Python tests, Creator Kit checks, and native offscreen integration checks. DMG mounting confirmed the packaged app matches the tested app; the app and DMG passed Developer ID signature verification.
- Developer ID–signed preview, not notarized. Long-duration observation, physical sleep/wake, and Intel runtime tests were not performed for this build.

## 1.4.77 — Cinderella memory update

Archived preview · Downloads withdrawn. [Download the current 1.4.87 preview](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg).

- Release hidden Cinderella scene textures after transitions, and restore them when needed. Image resolution, materials, and animation settings are preserved.
- In one local A/B test against 1.4.76 at the same display size, the warmed-up lobby observation median for the app and its attributed WebKit processes fell from 745.53 MiB to 673.53 MiB (72.00 MiB, about 9.7%). This is a short, scene-specific measurement, not a guarantee for every wallpaper or Mac.
- Passed 26 exact before/after frame comparisons, interaction and graphics-recovery checks, 65 Python tests, and release smoke checks. About eight minutes of installed dual-display observation showed one app instance, two wallpaper windows, and no newly logged faults in the monitored categories.
- Remove build-machine paths from debug symbols in the distributed executable.
- Developer ID–signed preview, not notarized. Long-duration, cross-device, Intel runtime, physical sleep/wake, and display hot-plug tests were not performed for this build.

## 1.4.74 — Signed preview

Archived preview · Downloads withdrawn. [Download the current 1.4.87 preview](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg).

- Developer ID–signed preview for macOS 13 or later, on Apple silicon and Intel. Apple notarization is not complete, so macOS may block the app when first opened.

- Star Citizen uses a still cover while browsing the review library, avoiding unnecessary simultaneous video playback. Selecting a cover does not need to start another video player.

## 1.4.73 — Review build

- Reworked the Hokucat cat scene, retaining pointer tracking, the draggable star, and its star trail.

## 简体中文

以上仅记录已核验的预览版变化，安装说明见[常见问题](docs/faq.md#简体中文)。

- **1.4.87 / build 97：** [下载已签名预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg) · [SHA-256 校验值](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/SHA256SUMS.txt)。将 Grok White、Grok Black、Muse、Clawd 合并为一个 **Characters（角色）** 入口，在预览旁直接选择角色，并原生切换黑白外观；**Hokucat** 独立保留手动颜色与自动颜色模式。新增原生 **Glass Clock**，可调整时区、尺寸、秒针与背景。补剂壁纸提供泡罩（blister）与磨砂（frosted）两种容器，并修正撤销和预览设置行为。默认库移除 Dots、SpongeBob、NIKKE2B、NIKKE4K01，**保留 NIKKE 灰姑娘**；历史演示素材保留来源署名。面向 macOS 13 或更新版本构建，包含 Apple 芯片与 Intel 架构；已使用 Developer ID 签名、未公证，Intel 实机运行未验证。本版不代表完整 PC 壁纸兼容性，也不代表已完成长时运行、整机睡眠唤醒与外屏拔插验收。

- **1.4.81：** 历史预览版，下载已撤回；[下载当前 1.4.87 预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg)。修复白猫耳尖、头顶和脸颊的多边形硬边，在加载时一次性合成原始毛发透明边缘，保留眨眼、追视和两屏贴图共享。同条件 60 秒离屏对照中，两个白猫视图所在进程的物理内存中位数从 62.36 MiB 降至 50.50 MiB，约减少 19%；该结果不涵盖实际双屏 GPU、WindowServer 和长期运行。通过可复现旧问题的边缘回归、4K 渲染、日夜切换、贴图释放、65 项 Python 测试、Creator Kit 和原生离屏集成检查，并在本机原生窗口核对了白猫效果。保留含 Last Horizon 的 13 项壁纸及原有署名和测试用标记。已签名、未公证；本版未重复长时、Intel 实机、睡眠唤醒和外屏拔插测试。

- **1.4.80：** 历史预览版，下载已撤回；[下载当前 1.4.87 预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg)。新增 Last Horizon，点击开合双眼，每次睁眼依次切换蓝瞳、琥珀瞳与猫瞳。以 8K 静态原画和经过适配的 1440p 原动画提供 4K 输出，动态底片经放大处理，并非原生 4K。静止时显示静态帧并释放视频播放器。保留贡献者署名、原始来源及两份上游 MIT 许可，详见[Last Horizon 署名](docs/credits.md#last-horizon)。已核对 19 份 Last Horizon 文件（16 份媒体的 SHA-256，以及来源记录与许可副本）和 13 项发行清单；通过 65 项 Python 测试、Creator Kit 与原生离屏集成检查，DMG 挂载确认包内应用与受测应用一致，应用和 DMG 的 Developer ID 签名验证通过。已签名、未公证；本版未补做长时观察、整机睡眠唤醒和 Intel 实机运行测试。

- **1.4.77：** 历史预览版，下载已撤回；[下载当前 1.4.87 预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg)。优化 Cinderella 隐藏场景的纹理释放与恢复，保留画质和互动。同尺寸本机 A/B 短时测试中，预热后大厅观察段的应用与关联 WebKit 物理内存中位数从 745.53 MiB 降至 673.53 MiB，减少约 9.7%。通过 26 组画面逐像素对照、互动与图形恢复检查、65 项 Python 测试和发布烟测；约八分钟双屏观察保持单实例、两个壁纸窗口，监测范围内未记录新故障。发行文件已清除构建目录信息。已签名、未公证；本版未补做长时、跨设备、Intel 实机、整机睡眠唤醒和外屏拔插测试。

- **1.4.74：** 历史预览版，下载已撤回；[下载当前 1.4.87 预览版](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.87/Hokucat-1.4.87.dmg)。支持 macOS 13 或更新版本以及 Apple 芯片和 Intel Mac，已使用 Developer ID 签名。Apple 公证尚未完成，macOS 可能阻止首次打开。浏览测试壁纸库中的 Star Citizen 时使用静态封面，避免仅选中封面就多开一路视频播放。
- **1.4.73：** 重做 Hokucat 小黑猫场景，保留鼠标追视、星星拖动和碎星轨迹互动。
