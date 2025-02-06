# Music Downloader

A Python script to search for songs on YouTube and download them as MP3.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/music_downloader.git
   cd music_downloader

2. Install dependencies
``` 
pip install -r requirements.txt
```

3. Ensure ffmpeg is installed on your system

## Usage

1. Add song names (one per line) to musicas.txt.
2. Run the script
```
python main.py
```
The script will:
1. Search for individual songs on YouTube.

2. Download the audio as MP3 files into the musicas/ folder.
3. If a YouTube playlist URL is provided, it will download all the videos in the playlist as MP3s.
4. Videos that are no longer available will be ignored, ensuring that the script continues to download the available videos in the playlist.