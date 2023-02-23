import moviepy.editor
from moviepy.editor import VideoFileClip
import os
import sys

video = VideoFileClip(r"vvv.mp4")
video.audio.write_audiofile(r"aaa.mp3")


