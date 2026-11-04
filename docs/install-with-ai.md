# Install Hokucat with AI

[Download manually](https://github.com/ar-gen-tin/hokucat/releases/tag/v1.4.74) · [简体中文](#中文安装提示词)

Give the prompt below to Codex, Claude Code, or Grok Bot running on your Mac with permission to download files and install apps. A chat without access to your Mac can explain the steps but cannot perform the installation.

**This preview is Developer ID–signed and is not notarized.** AI assistance does not change that status. If macOS blocks the first launch, you make the final decision in System Settings. No Apple account, AI API key, or password needs to be shared with Hokucat.

## Copy this prompt

```text
Install Hokucat on this Mac using the official installation guide:
https://github.com/ar-gen-tin/hokucat/blob/main/docs/install-with-ai.md

Follow its version and verification requirements. Check the official download,
SHA-256, Apple Developer ID signature, and installed app identity before launch.
Preserve my existing wallpaper library and settings. If an older Hokucat is
running, quit it normally before replacing it and keep a recoverable copy.
Retain macOS downloaded-file protections. If macOS blocks the first launch,
guide me through its normal confirmation and wait for me to approve it.
Do not disable security controls or remove quarantine attributes.
Report separately whether download, verification, installation, and launch
succeeded. Do not claim success while a system confirmation is still pending.
```

## What the assistant should do

1. Check that this is macOS 13 or later on Apple silicon or Intel. Check for an existing Hokucat installation and its running instance. Do not install a second copy or downgrade a newer version. If the same verified version is already installed, use it without replacing it.
2. Download the DMG and checksum file from the pinned release below over HTTPS. Prefer a browser download so macOS records the file's internet origin. Keep the download's quarantine metadata. If a terminal-only downloader does not attach that metadata, hand off the browser download instead of treating the missing protection as permission to run. Do not run scripts piped from the internet.
3. Verify the DMG's SHA-256 against **both** the value below and the release checksum file. Verify the DMG's Apple signature and expected Team ID. Stop if any check fails; do not remove a signature or sign the download again.
4. Mount the verified DMG read-only without opening its app. Verify `Hokucat.app` inside it: its signature, Team ID, bundle identifier, version, and build must match the table. Do not select an unrelated app or mount by a guessed volume name.
5. Before replacement, quit only the identified Hokucat instance normally and verify it has exited. If it will not quit, ask the user to close it; do not force-kill unrelated processes. Verify an existing same-named app's identity before moving it. If its identity differs or cannot be established, stop without moving it. Keep the old app in a recoverable backup outside Applications. Never delete or change the user's wallpaper library, preferences, or Application Support data as part of installation.
6. Copy the complete app bundle to `/Applications/Hokucat.app` using Finder's normal copy/replace flow, preserving extended attributes. Do not merge files into an existing `.app` bundle. Let macOS ask the user directly if administrator authorization is needed; do not request their password in chat or silently switch installation locations. If the existing installation is in another Applications folder, use that location rather than create a duplicate. Verify the installed app's identity and signature again and retain downloaded-file protection.
7. Open the installed app once through Finder or Launch Services, never by executing its inner binary to bypass the normal launch checks. If macOS blocks this unnotarized preview, explain the [first-launch confirmation](#first-launch-confirmation) and wait for the user. Do not repeatedly relaunch it or declare installation fully complete while confirmation is pending.
8. After any required approval, confirm that one Hokucat instance is running from the installed path and that **Wallpaper Dashboard** opens from its menu bar icon. Preserve the user's existing wallpaper choices. Eject only the DMG mounted for this installation. Report the installed version and any remaining user action.

The assistant must respect its own permission prompts. These instructions do not authorize changing system security policy, granting unrelated access, or reading personal files.

## Verified download

This guide pins a specific preview. Do not substitute a similarly named download, assume `/releases/latest` includes previews, or reuse these values for another version.

| Item | Expected value |
| --- | --- |
| Release | [v1.4.74 Preview](https://github.com/ar-gen-tin/hokucat/releases/tag/v1.4.74) |
| Installer | [Hokucat-1.4.74.dmg](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/Hokucat-1.4.74.dmg) |
| Checksum file | [SHA256SUMS.txt](https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/SHA256SUMS.txt) |
| Size | 133469919 bytes |
| SHA-256 | `cee9f80f6f5ed69644d574a7e716446ec644bd67da1472c90a4404944888b8eb` |
| Developer Team ID | `TVNJXB4Z9U` |
| Bundle identifier | `io.github.bodila51.grokbot-wallpaper` |
| App version / build | `1.4.74` / `82` |
| System | macOS 13 or later · Apple silicon or Intel |
| Distribution status | Developer ID–signed · Not notarized |

The bundle identifier retains the original project name for compatibility. The app name is **Hokucat**.

For an assistant with shell access, these are read-only verification commands. Set `DMG` to the observed downloaded file and `APP` to the app inside its verified mount; quote both paths. Check every command's exit status.

```sh
/usr/bin/shasum -a 256 "$DMG"
/usr/bin/codesign --verify --strict --verbose=2 \
  -R='anchor apple generic and certificate leaf[subject.OU] = "TVNJXB4Z9U" and certificate leaf[field.1.2.840.113635.100.6.1.13] exists' "$DMG"
/usr/bin/codesign --verify --deep --strict --verbose=2 \
  -R='anchor apple generic and certificate leaf[subject.OU] = "TVNJXB4Z9U" and certificate leaf[field.1.2.840.113635.100.6.1.13] exists and identifier "io.github.bodila51.grokbot-wallpaper"' "$APP"
/usr/libexec/PlistBuddy -c 'Print :CFBundleIdentifier' "$APP/Contents/Info.plist"
/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' "$APP/Contents/Info.plist"
/usr/libexec/PlistBuddy -c 'Print :CFBundleVersion' "$APP/Contents/Info.plist"
```

A matching hash proves the downloaded bytes match this release. A valid signature proves identity and integrity. Neither result proves Apple notarization or successful first launch. Do not describe a Gatekeeper rejection as a passed check merely because signature verification succeeded.

## First-launch confirmation

If macOS blocks this preview after an attempted launch, the user can review **System Settings → Privacy & Security → Open Anyway**, then confirm **Open**, if they choose to trust this verified download. Apple may require authentication. The user should enter credentials only in the macOS system prompt.

Do not disable Gatekeeper, delete quarantine attributes, change the system-wide app policy, or bypass an organization's device restrictions. If Apple reports malware, revoked authorization, or a damaged app, stop and report the exact message instead of recommending an override. See [Apple's guidance for downloaded apps](https://support.apple.com/en-us/102445).

## 中文安装提示词

把下面这段话交给**能操作你这台 Mac** 的 Codex、Claude Code 或 Grok Bot。纯网页聊天如果没有本机操作权限，只能提供指导。当前版本已签名、未公证，首次打开的系统确认仍由你完成。

```text
请在这台 Mac 上安装 Hokucat
先阅读官方安装指南并按里面的版本和校验要求执行
https://github.com/ar-gen-tin/hokucat/blob/main/docs/install-with-ai.md

从官方 GitHub Release 下载
核对 SHA-256 开发者签名和应用版本后再安装
保留我的壁纸库和设置
替换旧版前正常退出旧实例 并保留可恢复的旧版副本
保留 macOS 对下载文件的安全检查
如果首次启动被拦截 引导我在系统设置里确认并等我操作
不要关闭系统安全功能或移除隔离属性
分别告诉我下载 校验 安装和启动是否完成
需要我确认时不要把安装报告为全部完成
```

AI 可以协助下载、校验、安装和打开面板。安装过程不需要把 Apple 密码或 AI API key 发给它。若系统拦截，在你选择信任这份已核验的下载后，可进入 **系统设置 → 隐私与安全 → 仍要打开**，再按系统提示确认。公司管理设备的限制、恶意软件或文件损坏提示不应绕过。

其他语言用户可以请 AI 用自己的语言说明步骤，校验值和安全要求保持不变。
