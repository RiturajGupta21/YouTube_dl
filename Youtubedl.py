# importing modules
# Here youtube_dl will be used for downloading audio file
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox


# Method to select destination downloaded Audio file path
def setDownloadPath():
    # Location to initial download directory
    dwldDirectory = filedialog.askdirectory(
        initialdir="/Users/ritur/Downloads")
    # Setting the directory
    downloadPath.set(dwldDirectory)


# Downloading function
def download():
    # Get the videoLink from the link label
    youTube_Link = videoLink.get()
    # Fetching the downloading directory
    downloadFolder = downloadPath.get()
    # Setting the configuration for download file
    audiofiledowloadoptions = {
        # Setting download audio to be in best format
        'format': 'bestaudio/best',
        # Saving file name as title to destination
        'outtmpl': downloadFolder+"/%(title)s.%(ext)s",
        # Conversion of video to audio
        'postprocessors': [{
            # Extraction of audio from video
            'key': 'FFmpegExtractAudio',
            # Fromat of saved audio file
            'preferredcodec': 'mp3',
            # Bitrate quality of the sound
            'preferredquality': '320'
        }],
    }
    # Downloading the audio file using the module method
    # YoutubeDL() takes configuration as argument
    with youtube_dl.YoutubeDL(audiofiledowloadoptions) as audiodownload:
        # Link to the youtube video which have to be downloaded
        # YoutubeDL().download() takes link as argument
        audiodownload.download([youTube_Link])
    # Displaying the message
    messagebox.showinfo("Done", "Converted to Audio")


# creating tk class object
root = tk.Tk()
# Setting the size of the window
root.geometry("600x100")
# Disabling resizing property
root.resizable(False, False)
# Setting Title
root.title("Youtube Audio Downloader")
# Setting Background Color
root.config(background="black")
# Variables required
# Link variable
videoLink = StringVar()
# Download Path Variable
downloadPath = StringVar()
# Creating tkinter widgets
# YouTube Link Lable name
videolinkLabel = Label(root, text="YouTube Link :", bg="green")
# Poistioning of the label
videolinkLabel.grid(row=1, column=0, pady=5, padx=5)
# Textarea for the youtube link
YouTubeURLText = Entry(root, width=75, textvariable=videoLink)
# Poistioning of the Entry
YouTubeURLText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)
# Download folder Lable name
downloadpathLabel = Label(root, text="Donwload Location :", bg="green")
# Poistioning of the label
downloadpathLabel.grid(row=2, column=0, pady=5, padx=5)
# Textarea to show the download path folder
downloadpathText = Entry(root, width=50, textvariable=downloadPath)
# Poistioning of the Entry
downloadpathText.grid(row=2, column=1, pady=5, padx=5)
# Button to run the setDownloadPath method
pathsettingButton = Button(root, text="SetPath", command=setDownloadPath, width=15, bg="green")
# Poistioning of the Button
pathsettingButton.grid(row=2, column=2, pady=5, padx=5)
# Button to run the download method
dwldButton = Button(root, text="DOWNLOAD AUDIO", command=download, width=30, bg="green")
# Poistioning of the Button
dwldButton.grid(row=3, column=1, pady=5, padx=5)
# Infinite loop to run the program
root.mainloop()