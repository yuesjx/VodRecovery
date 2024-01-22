# Welcome to VodRecovery

This is a Fork of [VodRecovery](https://github.com/Shishkebaboo/VodRecovery) which is designed to retrieve Twitch Vods and Clips, containing a few adjustments.

## Installation and Setup

1. Download and install [Python](https://www.python.org/downloads/)
2. Download and install [FFmpeg](https://ffmpeg.org/download.html)
3. Clone this repository with: `git clone https://github.com/MacielG1/VodRecovery`
4. Navigate to the downloaded folder
5. Install the requirements by running `pip install -r requirements.txt` or the `install_dependencies.py` file
6. Run the program with: `python vod_recovery.py`

## Core Features

- Video Recovery: Choose between web-based or manual VOD recovery options.
- Clip Recovery: Recover clips manually or via mentioned websites.
- Random Clip Recovery: Retrieve a selection of random clips (3 clips per iteration).
- Multiple Formats: Recovered M3U8 links are available in various formats, including - chunked (Source Quality), 1080p60, 1080p30, 720p60, 720p30, 480p60, 480p30.
- Platform Compatibility: VodRecovery is compatible with popular platforms such as [TwitchTracker](https://twitchtracker.com/), [Sullygnome](https://sullygnome.com/), and [Streamscharts](https://streamscharts.com/).
- Bulk Clip Recovery: Easily recover multiple clips using CSV files from [Sullygnome](https://sullygnome.com/).
- Default Timezone: The script uses UTC as the default timezone for recovering VODs.

## Notes

- Ensure your Video requests comply with [Twitch's Video Retention Policy](https://help.twitch.tv/s/article/video-on-demand).
- Original Repo: [VodRecovery](https://github.com/Shishkebaboo/VodRecovery) by Shishkebaboo
