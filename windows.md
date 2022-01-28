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
yt-dlp -f "bv[ext=mp4]+ba[ext=m4a]/b[ext=mp4] <url>"
```
