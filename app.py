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