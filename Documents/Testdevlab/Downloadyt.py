import pytube
link = "" #Url of the
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()