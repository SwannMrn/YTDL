from __future__ import unicode_literals
import os
import io
import eel
import youtube_dl

eel.init('web')

def ytdl(data):
  link = data
  ydl_opts = {}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

eel.start('index.html', size=(1000, 600))