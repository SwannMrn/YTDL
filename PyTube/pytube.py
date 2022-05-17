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

def close_callback(route, websockets):
  if not websockets:
    exit()

eel.start('index.html', size=(1000, 600), close_callback=close_callback)
