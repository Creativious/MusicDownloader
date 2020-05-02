import speech_recognition as sr
import os
import time
import playsound
import search
import musicgrabber

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(f"User Said: {str(said)}")
        except Exception as e:
            print(f"Exception: {str(e)}")
    return said


def main():
    check_for = "hello"
    said = listen()
    vals = search.TestThing(said)
    firstVal = vals[0]
    path = musicgrabber.getMusic(firstVal)
    playsound.playsound(path)

main()