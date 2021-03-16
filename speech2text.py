import speech_recognition as sr
from gtts import gTTS
import os

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("speak :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, 7)

    try:

        text = r.recognize_google(audio)

        m = ("you said : {}".format(text))
        print(m)


    except:
        p = ("sorry! cant recognise your voice")
        
