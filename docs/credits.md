# Project lineage

Hokucat started from Codila's Grok Bot Wallpaper project. The direct upstream is [Bodila51/grokbot-wallpaper](https://github.com/Bodila51/grokbot-wallpaper). Its early history separates the [Bot HQ dashboard](https://github.com/Bodila51/grokbot-wallpaper/commit/e235531), the [browser wallpaper](https://github.com/Bodila51/grokbot-wallpaper/commit/8869e84), and the [macOS desktop host](https://github.com/Bodila51/grokbot-wallpaper/commit/3a910ef). The wallpaper and Mac commits credit Claude as a co-author.

The upstream wallpaper recreates the Grok Bot character's gaze and blink behavior in JavaScript. Its [white sphere preparation script](https://github.com/Bodila51/grokbot-wallpaper/blob/8869e84/assets/_src/face/make_sphere.py) identifies an approved ChatGPT frame as its source. The [black sphere](https://github.com/Bodila51/grokbot-wallpaper/commit/e13c01e) was rendered in Blender, with eyes adapted from the white version. The original macOS host places a WebKit window above the system wallpaper and behind Finder icons. On Windows the project used [Lively Wallpaper](https://github.com/lively-community/lively) to host its web wallpaper.

The default Hokucat cat wallpaper uses artwork made for Hokucat. From 1.4.73 it renders the cat, the sky, and the particles with macOS Core Animation.

## 中文

Hokucat 的 Mac 程序从 0xCodila 的 Grok Bot Wallpaper 项目发展而来。它的公开记录先有 3D 办公室看板，再加入网页壁纸和 macOS 桌面窗口。上游网页按 Grok Bot 的品牌动作重做追视和眨眼，白球源图来自一帧 ChatGPT 图像，黑球用 Blender 渲染并沿用改色的眼睛。Hokucat 默认的小黑猫是另做的壁纸，1.4.73 起使用 macOS Core Animation 绘制。
