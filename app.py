from googletrans import Translator
from os import path
from gtts import gTTS
import speech_recognition as sr


def lines(path):
    # Une fonction déstiner à lire dans un fichier
    # puis retourner les résultats dans une variable de
    # chaine de caractères
    file = open(path, "r")
    lines = file.readlines()
    for line in lines:
        line += line
    file.close()

    return line



# Obtenir l'audio à partir du micro
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Dites quelque chose... !")
    audio = r.listen(source)

# Ecrire l'audio au format .raw
with open("voices/voice.raw", "wb") as f:
    f.write(audio.get_raw_data())

# Ecrire l'audio au format .wav
# Un fichier binaire
with open("voices/voice.wav", "wb") as f:
    f.write(audio.get_wav_data())
