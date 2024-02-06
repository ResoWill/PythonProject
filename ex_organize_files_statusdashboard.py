import os
import shutil

# Define your directories and extensions here

# ... (The code you provided for defining source_directory, destination directories, and extensions)

def count_files(directory):
    return sum(1 for _ in os.listdir(directory))

if __name__ == "__main__":
    # Display the status dashboard
    print("=== Destination Directory Status ===")
    print(f"Videos: {count_files(video_directory)} files")
    print(f"Music: {count_files(music_directory)} files")
    print(f"Images: {count_files(image_directory)} files")
    print(f"Text Documents: {count_files(text_directory)} files")