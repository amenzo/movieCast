file1=open('createVideos.bat','w')
file1.write("ffmpeg -loop 1 -i nobody/poster.jpg -c:v libx264 -t 4 -pix_fmt yuv420p -vf scale=1200:720 videos/poster.mp4\n")
for i in range(13):
    file1.write("ffmpeg -loop 1 -i nobody/merged"+str(i)+".jpg -c:v libx264 -t 4 -pix_fmt yuv420p -vf scale=1200:720 videos/out"+str(i)+".mp4\n")
file1.close()
