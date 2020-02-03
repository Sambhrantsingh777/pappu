#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

from time import ctime
from listener import recordAudio
from speak_engine import speak
import os
import googletranslate


def pappu(query):
    if "how are you" in query:
        speak("I am fine")

    if "what time is it" in query:
        speak(ctime())

    if "where is" in query:
        query = query.split(" ")
        location = query[2]
        speak("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


# initialization
# time.sleep(2)
hindi = googletranslate.start("Aur batao?")
speak(hindi)

while True:
    query = recordAudio()
    pappu(query)
