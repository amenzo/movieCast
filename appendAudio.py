from moviepy.editor import VideoFileClip,concatenate_videoclips, CompositeVideoClip,AudioFileClip

audio = AudioFileClip("song.mp3")
audio=audio.subclip((0,0),(0,43))
video1 = VideoFileClip("outputM.mp4")
video2 = VideoFileClip("end.mp4")
final_clip=concatenate_videoclips([video1,video2])
final = final_clip.set_audio(audio)
i=13
final.write_videofile("final.mp4",codec= 'mpeg4' ,audio_codec='libvorbis')
