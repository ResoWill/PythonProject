# This script assumes that Downloads folder is the source directory.
# This script will go through the files in  Downloads folder and move them to the appropriate destination folders based on their file extensions. 
# Remember to replace the ~/Videos, ~/Music, ~/Pictures, and ~/Documents placeholders with your actual destination folder paths.
# Before running the script, make sure to back up your files in case anything goes wrong. 
# Additionally, test the script on a small set of files to ensure it behaves as expected before using it on your entire Downloads folder.

import os
import shutil

# Source directory (Downloads folder)
source_directory = os.path.expanduser("~/Downloads")

# Destination directories for different types of files
video_directory = os.path.expanduser("~/Videos")
music_directory = os.path.expanduser("~/Music")
image_directory = os.path.expanduser("~/Pictures")
text_directory = os.path.expanduser("~/Documents")

# List of video file extensions
video_extensions = [".mp4", ".mov", ".avi", ".mkv"]

# List of music file extensions
music_extensions = [".mp3", ".wav", ".flac"]

# List of image file extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

# List of text file extensions
text_extensions = [".txt", ".pdf", ".doc", ".docx"]

def organize_files(source, destination, extensions):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for file in os.listdir(source):
        if any(file.lower().endswith(ext) for ext in extensions):
            source_file_path = os.path.join(source, file)
            destination_file_path = os.path.join(destination, file)
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved '{file}' to '{destination}'")

if __name__ == "__main__":
    organize_files(source_directory, video_directory, video_extensions)
    organize_files(source_directory, music_directory, music_extensions)
    organize_files(source_directory, image_directory, image_extensions)
    organize_files(source_directory, text_directory, text_extensions)