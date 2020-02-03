import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from gtts import gTTS
from pygame import mixer
mixer.init()


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='hi')
    tts.save("audio.mp3")
    mixer.music.load("audio.mp3")
    mixer.music.play()