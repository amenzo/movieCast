from moviepy.editor import VideoFileClip,concatenate_videoclips, CompositeVideoClip
clips=[]
clip1=VideoFileClip("videos/poster.mp4")
print('appending poster')
clips.append(clip1)
for i in range(13):
    clip1=VideoFileClip("videos/out"+str(i)+".mp4")
    print('appending clip'+str(i))
    clips.append(clip1)
final_clip=concatenate_videoclips(clips)
final_clip.write_videofile('outputM.mp4')
