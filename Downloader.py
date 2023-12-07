# This is meant to be a video downloader where you input a link to a YT video and download it, however I keep getting SSL_certificate_verification errors (tried upgrading, network changing, debugging, etc but no luck)
# Code might be a little scrambled but should work, maybe just a network issue?

import tkinter as tk
from pytube import YouTube
import certifi
import os

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

def download_video():
    try:
        url = entry.get()
        youtube = YouTube(url)

        video = youtube.streams.filter(file_extension='mp4', res="720p").first()
        video.download()

        status_label.config(text="Download Successful!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def on_progress(stream, chunk, remaining):
    # You can customize the progress handling here if needed
    pass

def on_complete(stream, file_path):
    # You can customize the completion handling here if needed
    pass

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Entry widget for the YouTube URL
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Button to trigger the download
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=10)

# Label to display download status
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()