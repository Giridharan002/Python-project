from pytube import YouTube
import os
l=str(input("Paste Link here: "))
y=YouTube(l)
print("Your download take few minutes",y.title,".....")
output=y.streams.get_highest_resolution().download()
n=os.path.splitext(output)
os.rename(output,n[0]+".mp4")
print("Your Video",y.title," was Downloaded")
