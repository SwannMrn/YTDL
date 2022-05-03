from pytube import YouTube

link = input("Enter the link of the video: ")
yt = YouTube(link)

save_path = ''

def vid_info():
  print("Title: ",yt.title) # Title of video
  print("Author: ",yt.author) # author of the video
  print("Number of views: ",yt.views) # Number of views of video
  print("Length of video: ",yt.length," seconds")  # Length of the video
  print(yt.streams) # Printing all the available streams

audio = yt.streams.filter(only_audio=True) 
# audio only, ready to play

video = yt.streams.filter(only_video=True) 
# has no audio, must download separately, not ready to play

prog = yt.streams.filter(progressive="True") 
# progressive video has built in audio, ready to play

"""itag = int(input("Enter the itag of the stream you wish to download. "))

stream = yt.streams.get_by_itag(itag)
stream.download()"""

vid_info()