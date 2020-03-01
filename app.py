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


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "voices/voice.wav")
rec = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = rec.record(source)  # lecture entière du fichier audio

    # reconnaissance vocale utilisant Google Speech Recognition

try:
    # utilisation d'une clé API par défaut pour le test
    # si vous souhaitez utiliser une autre clé API, faites `rec.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # au lieu de `rec.recognize_google(audio)`
    print("Google Speech Recognition penses que vous avez dit :  " + rec.recognize_google(audio))
    with open("texts/translate/essai.txt", "w") as f:
        f.write(rec.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition n'a pas pu comprendre l'audio")
except sr.RequestError as e:
    print("Requête échoué du service Google Speech Recognition : {0}".format(e))



translator = Translator()
line = lines('texts/translate/essai.txt')
lang = translator.detect(line)
print(lang.lang)

