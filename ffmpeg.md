FFmpeg commands work identically in Windows Command Prompt (cmd.exe) or PowerShell once installed and added to PATH. Open cmd by pressing Win+R, typing "cmd", and pressing Enter, then use cd to navigate to your video folder (e.g., cd C:\Videos).

## Installation on Windows
Download FFmpeg from gyan.dev/ffmpeg/builds, extract to C:\ffmpeg, and add C:\ffmpeg\bin to system PATH via Environment Variables.
Verify with: `ffmpeg -version` in cmd.
PowerShell script option: Run `Invoke-WebRequest -Uri "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip" -OutFile "ffmpeg.zip"; Expand-Archive ffmpeg.zip -DestinationPath C:\; Rename-Item (Get-ChildItem C:\ -Filter ffmpeg-*-essentials* -Directory).FullName ffmpeg` then add to PATH.

## Clipping MP4 Videos
clips 30s from 1:30
```
ffmpeg -ss 00:01:30 -i input.mp4 -t 00:00:30 -c copy output.mp4
``` 
from 10s to end
```
ffmpeg -ss 00:00:10 -i input.mp4 -c:v copy -c:a copy trimmed.mp4
```
Multiple clips: Create segments with above (name output1.mp4, output2.mp4), then 
```
ffmpeg -f concat -i inputs.txt -c copy final.mp4
``` 
where inputs.txt lists file 'output1.mp4' etc.

## Converting AVI to MP4
```
ffmpeg -i input.avi -c:v copy -c:a copy output.mp4
``` 
(fast stream copy).
```
ffmpeg -i input.avi -c:v libx264 -c:a aac output.mp4
``` 
(re-encode for compatibility).
High quality: 
```
ffmpeg -i input.avi -c:v libx264 -preset slow -crf 19 -c:a aac -b:a 128k output.mp4
```

## Batch Conversion
In cmd: 
```
for %i in (*.avi) do ffmpeg -i "%i" "%~ni.mp4"
``` 
(all AVI files in folder).

