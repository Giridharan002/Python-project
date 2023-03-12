

from pytube import YouTube
import os
link = str(input())
video = YouTube(link)
print('Title: ', video.title)
print("This should only take a few seconds.....")

x = video.streams.filter(only_audio=True).first().download()
n = os.path.splitext(x)
os.rename(x, n[0]+'.mp3')
print(video.title, "was downloaded")
