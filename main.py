import os
from music_downloader.downloader import process_music_list


def main():
    """Entry point of the script."""
    file_path = "musicas.txt"

    if not os.path.exists(file_path):
        print("Error: 'musicas.txt' file not found. Please create the file and add song names.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        songs = [line.strip() for line in f.readlines() if line.strip()]

    if not songs:
        print("Warning: 'musicas.txt' is empty. Please add at least one song title.")
        return

    print("Starting music download process...")
    process_music_list(file_path)
    print("All downloads completed.")


if __name__ == "__main__":
    main()