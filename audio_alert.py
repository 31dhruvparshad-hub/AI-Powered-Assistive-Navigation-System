import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

from audio_alert import speak

speak("Navigation system started")