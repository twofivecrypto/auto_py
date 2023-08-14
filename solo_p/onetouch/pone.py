import pytube import Youtube
import os
import speech_recognition as sr
from gtts import gTTS
import pygame

def download_video(url, save_path):
    #DOWNLOAD THE YOUTUBE VIDEO
    yt = Youtube(url)
    video = yt.streams.get_audio_only()
    video.download(output_path=save_path)

def extract_audio(video_path, audio_path):
    #EXTRACT AUDIO FROM VIDEO
    #MIGHT NEED ANOTHER LIBRARY LIKE MOVIEPY OR FFMPEG TO DO THIS
    #EXTRACT THE AUDIO AND SAVE IT IN audio_path

def convert_audio_to_text(audio_path):
    #Initialize recognizer
    recognizer = sr.Recognizer()
    #LOAD AUDIO FILE
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

        #CONVERT AUDIO TO TEXT
