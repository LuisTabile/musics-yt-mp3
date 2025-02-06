import os
import yt_dlp


def ensure_music_folder():
    """Ensure the 'musicas' directory exists."""
    os.makedirs("musicas", exist_ok=True)


def search_youtube(query):
    """Search YouTube using yt-dlp and return the first video URL.
    Try searching with 'lyrics' first, then without if no result is found."""
    try:
        for attempt in [f"{query} lyrics", query]:
            search_url = f"ytsearch:{attempt}"
            ydl_opts = {
                'quiet': True,
                'default_search': 'ytsearch',
                'noplaylist': True,
                'extract_flat': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(search_url, download=False)
                if 'entries' in info and info['entries']:
                    return info['entries'][0]['url']
            print(f"⚠️ No results found for: {attempt}")
        return None
    except Exception as e:
        print(f"❌ Error searching for {query}: {e}")
        return None


def download_audio(url, title):
    """Download audio from YouTube using yt-dlp."""
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join("musicas", f"{title}.mp3"),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Download completed: {title}.mp3")
    except Exception as e:
        print(f"❌ Error downloading {title}: {e}")


def process_music_list(file_path):
    """Read the music list from a file and download each song."""
    if not os.path.exists(file_path):
        print("❌ Error: music list file not found.")
        return

    ensure_music_folder()

    with open(file_path, "r", encoding="utf-8") as f:
        songs = [line.strip() for line in f.readlines() if line.strip()]

    if not songs:
        print("⚠️ Warning: The music list is empty.")
        return

    for song in songs:
        print(f"🔍 Searching for: {song}")
        url = search_youtube(song)
        if url:
            download_audio(url, song)
        else:
            print(f"⚠️ No results found for: {song}")
