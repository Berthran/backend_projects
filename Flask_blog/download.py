from pytube import YouTube 

# where to save 
SAVE_PATH = "/mnt/c/Users/HP/Downloads/"

# link of the video to be downloaded 
link = "https://www.youtube.com/watch?v=tdIIJuPh3SI"

try: 
    # object creation using YouTube 
    print("Creating link...")
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files
print("Get all streams and filter for mp4 files...")
mp4_streams = yt.streams.filter(file_extension='mp4').all()

# get the video with the highest resolution
print("get the video with the highest resolution")
print("Quality:", mp4_streams)
d_video = mp4_streams[-1]

# try: 
#     # downloading the video 
#     d_video.download(output_path=SAVE_PATH)
#     print('Video downloaded successfully!')
# except: 
#     print("Some Error!")

