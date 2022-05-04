from pytube import YouTube

link = input("Enter the link of the video: ")
yt = YouTube(link)

save_path = ''

def vid_title():
  return yt.title

def vid_author():
  return yt.author

def vid_length():
  return yt.length

def vid_publishdate():
  return yt.publish_date

def vid_title():
  return yt.title

def vid_views():
  return yt.views

def vid_desc():
  return yt.description

def vid_streams():
  return yt.streams

def audio_streams():
  audio = yt.streams.filter(only_audio=True) 
  # audio only, ready to play
  return audio

def video_streams():
  video = yt.streams.filter(only_video=True) 
  # has no audio, must download separately, not ready to play
  return video

def progressive_streams():
  prog = yt.streams.filter(progressive="True") 
  # progressive video has built in audio, ready to play
  return progressive

def download():
  print(vid_streams)
  itag = int(input("Enter the itag of the stream you wish to download. "))
  stream = yt.streams.get_by_itag(itag)
  stream.download()
  return none

download()