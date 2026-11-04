#!/usr/bin/env python3
"""Make a Hokucat Package v1 folder with a silent video and two stills."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory


ENTRY = "media/loop.mp4"
PREVIEW = "media/preview.png"
FALLBACK = "media/still.png"
RIGHTS = "rights/assets.json"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="new package folder")
    parser.add_argument("--source", type=Path, help="local MP4, MOV, or M4V you may use and adapt")
    parser.add_argument("--attribution", help="credit for the source video and derived stills")
    args = parser.parse_args()
    output = args.output.expanduser().absolute()
    if output.exists() or output.is_symlink() or not output.parent.is_dir():
        parser.error("choose a new output folder inside an existing directory")
    for name in ("ffmpeg", "ffprobe"):
        if not shutil.which(name):
            parser.error(f"install {name} and make it available on PATH")

    try:
        source = None
        title = "Quiet Tide"
        package_id = "example.quiet-tide"
        author = "Hokucat Examples"
        attribution = "Original procedural artwork rendered by the Hokucat example"
        if args.source:
            source = args.source.expanduser().resolve(strict=True)
            if not source.is_file() or source.suffix.lower() not in {".mp4", ".mov", ".m4v"}:
                parser.error("--source must point to a local MP4, MOV, or M4V file")
            attribution = (args.attribution or "").strip()
            has_control = any(ord(char) < 32 or ord(char) == 127 for char in attribution)
            if not attribution or len(attribution) > 120 or has_control:
                parser.error("--source needs a single-line --attribution of 1–120 characters")
            duration = float(probe(source)["format"].get("duration", 0))
            if not 0 < duration <= 1200:
                parser.error("the source video must run for more than zero and at most 20 minutes")
            package_id = source_id(source)
            title = "Imported video"
            author = "Local creator"
        elif args.attribution is not None:
            parser.error("--attribution requires --source")

        with TemporaryDirectory(prefix=".hokucat-", dir=output.parent) as scratch:
            package = Path(scratch) / "package"
            (package / "media").mkdir(parents=True)
            (package / "rights").mkdir()
            video = package / ENTRY
            render_video(video, source)
            width, height = check_video(video)
            ffmpeg("-i", video, "-frames:v", "1", "-update", "1", package / FALLBACK)
            ffmpeg("-i", video, "-vf", "scale=w='min(640,iw)':h=-1",
                   "-frames:v", "1", "-update", "1", package / PREVIEW)
            manifest = {
                "schemaVersion": 1,
                "id": package_id,
                "version": "1.0.0",
                "title": title,
                "author": {"name": author},
                "license": RIGHTS,
                "preview": PREVIEW,
                "fallback": FALLBACK,
                "renderer": "video",
                "entry": ENTRY,
                "recommendedResolution": {"width": width, "height": height},
                "parameters": {"fit": "fill", "playbackRate": 1},
            }
            rights = {"assets": [
                {"path": path, "attribution": attribution, "usage": True, "adaptation": True, "distribution": False}
                for path in (ENTRY, PREVIEW, FALLBACK)
            ]}
            write_json(package / "manifest.json", manifest)
            write_json(package / RIGHTS, rights)
            if sum(path.stat().st_size for path in package.rglob("*") if path.is_file()) > 512 * 1024**2:
                raise ValueError("package exceeds the 512 MiB limit")
            output.mkdir()  # Reserve the name without overwriting an existing folder.
            try:
                package.replace(output)
            except OSError:
                output.rmdir()
                raise
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Could not make wallpaper: {error}\n")
    print(f"Created {output}")


def render_video(path, source):
    if source:
        scale = ("scale=w='min(1920,iw)':h='min(1080,ih)':"
                 "force_original_aspect_ratio=decrease:force_divisible_by=2")
        inputs = ["-protocol_whitelist", "file", "-f", "mov", "-i", source,
                  "-map", "0:V:0", "-vf", scale]
    else:
        sky = ("gradients=s=640x360:r=30:d=8:n=4:c0=0x060D1C:c1=0x101F34:"
               "c2=0x234655:c3=0x0E293B:x0=0:y0=0:x1=0:y1=359:speed=0")
        light = ("gradients=s=400x400:r=30:d=8:c0=0x7AD9CF@0.63:c1=0x7AD9CF@0:"
                 "x0=200:y0=200:x1=386:y1=200:type=radial:speed=0")
        motion = ("[1:v]format=rgba,scale=400:48[glow];"
                  "[0:v][glow]overlay=x='(W-w)/2+84*sin(2*PI*t/8)':y=222,scale=1920:1080[out]")
        inputs = ["-f", "lavfi", "-i", sky, "-f", "lavfi", "-i", light, "-filter_complex", motion, "-map", "[out]"]
    ffmpeg(*inputs, "-an", "-map_metadata", "-1", "-map_chapters", "-1", "-c:v", "libx264", "-preset", "fast",
           "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", path)


def check_video(path):
    data = probe(path)
    streams = data["streams"]
    if len(streams) != 1 or streams[0]["codec_type"] != "video" or streams[0]["codec_name"] != "h264":
        raise ValueError("expected one H.264 video stream and no audio")
    if not 0 < float(data["format"].get("duration", 0)) <= 1200:
        raise ValueError("the output video must run for more than zero and at most 20 minutes")
    return streams[0]["width"], streams[0]["height"]


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", *args], check=True)


def probe(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-protocol_whitelist", "file", "-f", "mov",
         "-show_entries", "stream=codec_type,codec_name,width,height:format=duration", "-of", "json", path],
        check=True, capture_output=True, text=True,
    )
    return json.loads(result.stdout)


def source_id(source):
    digest = hashlib.sha256()
    with source.open("rb") as video:
        for block in iter(lambda: video.read(1024 * 1024), b""):
            digest.update(block)
    return "local.video-" + digest.hexdigest()[:16]


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
