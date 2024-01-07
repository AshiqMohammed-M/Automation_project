'''wanna install pytube,moviepy os and shutil pakage before use'''


from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os, shutil


def adaptive(url, res):
    yt = YouTube(url)

    print("downloading video file")

    size = yt.streams.filter(adaptive=True).get_by_itag(res).filesize
    print(size * 0.000001, "MB")
    yt.streams.filter(adaptive=True).get_by_itag(res).download("video.mp4")
    print("v complete")

    print("downloading audio file")

    yt.streams.filter(only_audio=True).first().download("audio.mp4")
    print("a complete")

    videopath = os.path.realpath("video.mp4")
    audiopath = os.path.realpath("audio.mp4")

    filename = YouTube(url).title
    videofolder = (videopath + "\\" + yt.title + ".mp4")
    audiofolder = (audiopath + "\\" + yt.title + ".mp4")

    # Open the video and audio
    video_clip = VideoFileClip(videofolder)
    audio_clip = AudioFileClip(audiofolder)

    # Concatenate the video clip with the audio clip
    final_clip = video_clip.set_audio(audio_clip)

    title = input("Enter the title for your video")

    # Export the final video with audio
    final_clip.write_videofile(title + ".mp4")

    # removing unwanted vidio and audio file
    shutil.rmtree("audio.mp4")
    shutil.rmtree("video.mp4")

    return 0


def progressive(url, res):  # for 360p & 720p only
    print("hello")
    yt = YouTube(url)

    yt.streams.filter(progressive=True).get_by_resolution(res).download()

    return 0


url = input("enter the URL:")

# resolution : itag value in pytube
resolutions = {
    "144p": 17,
    "240p": 133,
    "360p": 18,
    "480p": 135,
    "720p": 22,
    "1080p": 137,
    "1440p": 271,
    "2160p": 313
}

res = input("Enter the resolution (eg:'720p') : ")

if res == "720p" or res == "360p":
    progressive(url, resolutions[res])

else:
    adaptive(url, resolutions[res])
