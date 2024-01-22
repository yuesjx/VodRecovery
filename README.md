# Welcome to VodRecovery

This is a Fork of [VodRecovery](https://github.com/Shishkebaboo/VodRecovery) which is designed to retrieve Twitch Vods and Clips and includes a few adjustments.

## Installation and Setup

1. Download and install [Python](https://www.python.org/downloads/).
2. Download and install [FFmpeg](https://ffmpeg.org/download.html)
3. Clone this repository with: `git clone https://github.com/MacielG1/VodRecovery`
4. Navigate to the downloaded folder.
5. Install the requirements by running the file `install_dependencies..py` or typing `pip install -r requirements.txt`
6. Run the program with: `python vod_recovery.py`

## Core Features

- Video Recovery: Choose between manual or web-based VOD recovery options.
- Clip Recovery: Recover clips manually or via mentioned websites.
- Bulk Clip Recovery: Easily recover multiple clips using CSV files from [Sullygnome](https://sullygnome.com/).
- Random Clip Recovery: Retrieve a selection of random clips (3 clips per iteration).
- Multiple Formats: Recovered M3U8 links are available in various formats, including - chunked (Source Quality), 1080p60, 1080p30, 720p60, 720p30, 480p60, 480p30
- Platform Compatibility: VodRecovery is compatible with popular platforms such as [TwitchTracker](https://twitchtracker.com/), [Sullygnome](https://sullygnome.com/), and [Streamscharts](https://streamscharts.com/).
- Default Timezone: The script uses UTC as the default timezone for recovering VODs.
- Video Expiry Duration: Receive a notification if a VOD is older than 60 days, helping you stay informed about content availability.

## Notes

- Ensure your Video requests comply with [Twitch's Video Retention Policy](https://help.twitch.tv/s/article/video-on-demand).
- Original Repo: [VodRecovery](https://github.com/Shishkebaboo/VodRecovery) by Shishkebaboo
