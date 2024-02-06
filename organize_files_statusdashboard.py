import os
import shutil

# Define your directories and extensions here
# ... (The code you provided for defining source_directory, destination directories, and extensions)

# Source directory (Downloads folder)
source_directory = os.path.expanduser("/Users/Resowill/Downloads")

# Destination directories for different types of files
video_directory = os.path.expanduser("/Users/Resowill/Documents/Job Search/Python Projects/Local File Automation Project/Automated Files/Videos")
music_directory = os.path.expanduser("/Users/Resowill/Documents/Job Search/Python Projects/Local File Automation Project/Automated Files/Music")
image_directory = os.path.expanduser("/Users/Resowill/Documents/Job Search/Python Projects/Local File Automation Project/Automated Files/Pictures")
text_directory = os.path.expanduser("/Users/Resowill/Documents/Job Search/Python Projects/Local File Automation Project/Automated Files/Documents")

# List of video file extensions
video_extensions = [".mp4", ".mov", ".avi", ".mkv"]

# List of music file extensions
music_extensions = [".mp3", ".wav", ".flac"]

# List of image file extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

# List of text file extensions
text_extensions = [".txt", ".pdf", ".doc", ".docx"]

def count_files(directory):
    return sum(1 for _ in os.listdir(directory))

if __name__ == "__main__":
    # Display the status dashboard
    print("=== Destination Directory Status ===")
    print(f"Videos: {count_files(video_directory)} files")
    print(f"Music: {count_files(music_directory)} files")
    print(f"Images: {count_files(image_directory)} files")
    print(f"Text Documents: {count_files(text_directory)} files")