# Make an animated Hokucat wallpaper with AI

Use Codex or Claude Code to render a short animation from code, or bring a video exported from a tool you already use. Turn the result into a local Hokucat Package v1 folder, then preview it in the Wallpaper Dashboard and choose where to apply it.

## Start with an original animation

Open Codex or Claude Code in an empty working folder. Give it this prompt, or change the scene to suit your desktop. [Codex setup](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) · [Claude Code setup](https://code.claude.com/docs/en/overview)

```text
Create an original 8-second desktop wallpaper called Quiet Tide. Use Python
or FFmpeg to render a fixed dark-blue horizon with soft moving reflections.
Keep the top half quiet for desktop icons. Use no downloaded assets, logos,
characters, text, or audio. Make all motion periodic over exactly eight
seconds and omit the duplicate end frame so the loop has a clean seam.
Export quiet-tide.mp4 as 1920 × 1080, 30 fps, H.264, yuv420p, with no audio
track. Use FFprobe to report its codec, dimensions, duration and streams.
Keep the source files and video local. Leave the desktop as it is.
```

You can also ask ChatGPT to help plan the animation, write a rendering script, or create an original still. To animate a still without a video generation service, ask Codex or Claude Code to render a slow pan, light shift, or other periodic motion from it. If you already have a video export, use that file as your source. Preview the cut between the last and first frames. Transcoding removes audio and standardizes the video. A visible jump still needs an edit to the motion or trim. [Images in ChatGPT](https://help.openai.com/en/articles/11084440-images-in-chatgpt)

## Make the import folder

With Python 3 and FFmpeg (including `ffprobe` and the `libx264` encoder) installed, run this from the public Hokucat repository. Use a folder name that is not already in use.

```sh
python3 examples/make-wallpaper.py "$HOME/quiet-tide"
```

This generates an original 8-second demo loop. To turn your own authorized video export into a package, run the same tool with `--source` and credit the source. The script preserves the video cadence, removes the audio track, and saves an image from the first frame for the preview and fallback.

```sh
python3 examples/make-wallpaper.py "$HOME/my-wallpaper" \
  --source ./quiet-tide.mp4 --attribution "Original video by Your Name"
```

A video package is a folder containing these files. Select the folder in Hokucat, with `manifest.json` at its top level.

```text
quiet-tide/
├── manifest.json
├── media/
│   ├── loop.mp4
│   ├── preview.png
│   └── still.png
└── rights/
    └── assets.json
```

The preview is the image shown in the library. The fallback is the still Hokucat can use if the video cannot play. Both can come from a representative frame. Use package-relative paths and keep the `id` stable when you publish a new revision of the same work.

```json
{
  "schemaVersion": 1,
  "id": "example.quiet-tide",
  "version": "1.0.0",
  "title": "Quiet Tide",
  "author": { "name": "Example Studio" },
  "license": "rights/assets.json",
  "preview": "media/preview.png",
  "fallback": "media/still.png",
  "renderer": "video",
  "entry": "media/loop.mp4",
  "recommendedResolution": { "width": 1920, "height": 1080 },
  "parameters": { "fit": "fill", "playbackRate": 1 }
}
```

List `media/loop.mp4`, `media/preview.png`, and `media/still.png` in the `assets` array of `rights/assets.json`. Each record has `path`, `attribution`, `usage`, `adaptation`, and `distribution`. Use your actual source and rights for every file, including any source used to create the preview or fallback. Local import requires `usage: true`. Keep `distribution: false` when permission to redistribute is unconfirmed.

### Creator Kit from a Hokucat source checkout

On macOS 13 or later with Xcode or the Command Line Tools, run these commands from a Hokucat source checkout. The destination must be a new folder with an existing parent directory.

```sh
bash mac/creator.sh init-video "$HOME/quiet-tide"
```

Replace the starter video, preview, and still with your work. For the `quiet-tide.mp4` export above, run these commands with FFmpeg installed. They replace the three sample media files in the new starter folder.

```sh
package="$HOME/quiet-tide"
ffmpeg -y -i quiet-tide.mp4 -map 0:v:0 -an -c:v libx264 -pix_fmt yuv420p \
  -movflags +faststart "$package/media/loop.mp4"
ffmpeg -y -i "$package/media/loop.mp4" -frames:v 1 -update 1 "$package/media/still.png"
ffmpeg -y -i "$package/media/loop.mp4" -vf scale=640:-2 -frames:v 1 -update 1 \
  "$package/media/preview.png"
```

Update the title, ID, author, recommended resolution, and rights declarations to match your files. Validate the finished package with the app's importer in temporary storage.

```sh
bash mac/creator.sh validate "$HOME/quiet-tide" --json
```

## Try it on your Mac

In an installed Hokucat build with Package v1 support, open **Wallpaper Dashboard → Import…** and select the package folder. Preview it, choose a display, and click **Apply Wallpaper**. Watch through at least two loop boundaries and check how the wallpaper crops on the display you chose.

Package v1 accepts PNG or JPEG stills and silent MP4, MOV, or M4V loops. The desktop plays the packaged media locally. The AI assistant is a creation tool for this workflow. Interactive Web and Windows Scene projects, audio input, and live pointer, API, or agent input are outside the v1 format.

## 中文快速开始

安装 Python 3 和带有 H.264 编码器的 FFmpeg，确保终端能运行 `ffmpeg` 和 `ffprobe`。在本仓库目录下生成一个可导入的 8 秒示例。

```sh
python3 examples/make-wallpaper.py "$HOME/quiet-tide"
```

也可以把创作提示词交给 Codex 或 Claude Code，让它在本机生成原创循环视频。ChatGPT 可用于写分镜、生成原创静帧或草拟动效脚本。拿到已有视频后，用下面的命令去掉音轨，并生成图库预览、回退图和作品清单。

```sh
python3 examples/make-wallpaper.py "$HOME/my-wallpaper" \
  --source ./my-video.mp4 --attribution "原创视频，作者填这里"
```

示例提示词

```text
创作一个 8 秒的原创夜空壁纸。给桌面图标留出空间，让暖色光晕在画面下半部分缓慢移动。
所有动作以 8 秒为周期，去掉重复的最后一帧。仅使用原创素材，不加文字、标志或音轨。
导出 1920×1080、30fps 的 H.264 MP4，检查视频参数和循环接缝。
```

在已安装的 Hokucat 里选择「壁纸面板 → 导入…」，选中整个作品文件夹，然后预览并应用。AI 参与的是创作阶段，应用播放的是导入后的本机视频。Package v1 的公开示例使用静音循环视频。
