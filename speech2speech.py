"""
    this code repeats whatever you say:
    but it requires a net connection as it uses google api

"""

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("speak :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
        engine.say("you said : {}".format(text))
        engine.runAndWait()

    except:
        engine.say("sorry! cant recognise your voice")
        engine.runAndWait()
