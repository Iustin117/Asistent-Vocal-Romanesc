import speech_recognition as sr
from gtts import gTTS
from time import sleep
import os
import pyglet

###Raspuns###
def raspuns(text):

    tts = gTTS(text = text, lang = 'ro')
    filename = 'temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove(filename) #remove temperory file



####Recunoastere vocala####
def recunoastere_vocala(r):

    with sr.Microphone() as source:
        print("Spune orice:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ro-RO")
        except sr.RequestError:
            print("Problema cu API-ul")
        except sr.UnknownValueError:
            print("Vocea nu a putut fi inteleasa...")

    return text


###youtube search###
def youtube():
    raspuns("")


if __name__ == "__main__":
    r = sr.Recognizer()
    comanda = recunoastere_vocala(r)
    dictionar_comenzi = ['youtube','notificari','ce mai faci']
    print('{}'.format(comanda))
    for com in dictionar_comenzi:
        comanda_recunoscuta = str(comanda).lower() == com.lower()
        if comanda_recunoscuta:
            salut = raspuns("Salut! Cum te simti?")
            break
    raspuns("Nu am înțeles ce ai spus.")
