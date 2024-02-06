# Simple example of how you could create a basic GUI using the Tkinter library
# in Python to call your organize_files.py script and display the status dashboard.
# Minimal example, and you might need to adapt and expand it based on your needs.
# Remember that this example uses the os.system("python organize_files.py") command to run your script.
# If your script has dependencies or is more complex, you might want to use other approaches to run it, such as using subprocess.
# This is a very basic example, and you can further customize the GUI, add more features, and improve its appearance using Tkinter's capabilities.
# If you're looking for more sophisticated GUI frameworks, you might explore libraries like PyQt or Kivy.

import os
import shutil
import tkinter as tk
from tkinter import messagebox


# Define your directories and extensions here
# ... (The code you provided for defining source_directory, destination directories, and extensions)

# ... (Your script code here)

# Function to run the organize_files.py script and display the status
def run_script_and_display_status():
    # Run the organize_files.py script
    os.system("python organize_files.py")

    # Display a message box with the status
    message = (
        f"Videos: {count_files(video_directory)} files\n"
        f"Music: {count_files(music_directory)} files"
    )
    messagebox.showinfo("Status Dashboard", message)


# Create the GUI window
window = tk.Tk()
window.title("File Organizer Dashboard")

# Create a button to run the script and display status
run_button = tk.Button(window, text="Run Script and Display Status", command=run_script_and_display_status)
run_button.pack()

# Start the GUI event loop
window.mainloop()