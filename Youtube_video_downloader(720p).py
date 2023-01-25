from pytube import YouTube  # pip install pytube


# Function to download the video
def download(vid):
    # object creation using YouTube
    youtube_object = YouTube(vid)
    # Download the video in 720p
    youtube_object = youtube_object.streams.get_by_resolution("720p")
    try:
        # Download the video.
        youtube_object.download()
        print("video Downloaded successfully")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


try:
    # Enter the YouTube link.
    link = input("Enter the YouTube video URL: ")
    download(link)
except:
    print("Please enter a valid link")
