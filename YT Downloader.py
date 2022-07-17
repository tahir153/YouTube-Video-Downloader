from pytube import YouTube
link = input("Enter URL: ")
video = YouTube(link)
print("Your Video Is Downloading...")
stream = video.streams.get_highest_resolution()
stream.download()
print("Your Video is Downloaded!!!")