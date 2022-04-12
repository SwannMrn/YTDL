from pytube import YouTube  # Make sure to have PyTube installed. If not, copy/paste this line in cmd.
### pip install pytube3 ###

link = input(“Enter the link: “)
yt = YouTube(link)


def vid_info():
  print(“Title: “,yt.title) # Title of video
  print(“Number of views: “,yt.views) # Number of views of video
  print(“Length of video: “,yt.length,”seconds”)  # Length of the video
  print("Description: ",yt.description) # Description of video
  print("Ratings: ",yt.rating)  #Rating
  print(yt.streams) # Printing all the available streams

def audiovideo():
  x = int(input("Type 1 for video downloads, or 2 for audio downloads. >>> "))
  if x == 2:
    print(yt.streams.filter(only_audio=True))
  elif x == 1:
    print(yt.streams.filter(only_video=True))

