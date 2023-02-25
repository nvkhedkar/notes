# Windows OS Notes

## Services
To find status of services loading at startup:
- run `services.msc` from start -> search bar - This will open dialog which has all services listed
## WSL 2 stuff
1. [Cool things in wsl](https://www.hanselman.com/blog/CoolWSLWindowsSubsystemForLinuxTipsAndTricksYouOrIDidntKnowWerePossible.aspx)
2. [Wsl 2 developers guide](https://www.sitepoint.com/wsl2-windows-terminal/)

## Open sound settings
Run in the search bar
```
mmsys.cpl
```

## yt-dlp
Just download:
```
yt-dlp <url>
```
This downloads the best video.  
To see types of files:
```
yt-dlp -F <url>
```
combine best video and audio
```
yt-dlp -f "bv[ext=mp4]+ba[ext=m4a]/b[ext=mp4]" <url>
```
combine best mp4 video with filesize < 1500M and audio
```
yt-dlp -f "bv[filesize<1500M][ext=mp4]+ba[ext=m4a]/b[ext=mp4]" <url>
```
combine best mp4 video with 720p resolution and audio and format output to include timestamp
```
yt-dlp -f "bv[height=720][ext=mp4]+ba[ext=m4a]/b[ext=mp4]" <url> -o "%(title)s-%(upload_date)s.%(ext)s"
```

combine best video and audio - and convert only to mp3
```
yt-dlp -f "bv[ext=mp4]+ba[ext=m4a]/b[ext=mp4]" -x --audio-format mp3 <url>
```
