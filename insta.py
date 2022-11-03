from pytube import YouTube

url = 'https://youtu.be/EAYlckSaviI'

yutube_1= YouTube(url)
video = yutube_1.streams.all()
vid = list(enumerate(video))
for i in vid:
    print(i)



strm = int(input("enter : "))
video[strm].download()
print('Successfully dowloanding')






