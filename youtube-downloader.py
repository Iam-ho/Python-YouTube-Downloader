import pytube

# The Video well be save in the following Directory
download_loc = './'

# Ask the user to enter the URL of the YouTube
Video_URL = input("PLZ enter URL: ")

# Creat an instance of YouTube Video
video_instance = pytube.YouTube(Video_URL)

stream = video_instance.streams.get_highest_resolution()

# Downloading ...
Downloading = "Downloading..."
print(Downloading)

# Download
stream.download()

# Download finished
Finished = "Download Complete"
print(Finished)
