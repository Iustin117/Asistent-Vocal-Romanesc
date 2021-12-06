from googlesearch import search
import speech_recognition as sr
from gtts import gTTS
from time import sleep
import os
import pyglet
import webbrowser
from bs4 import BeautifulSoup
import urllib

###dictionare
dictionar_google = ['google','caută pe google','gaseste pe google','caută ceva pentru mine','caută',"spune și mie"]
dictionar_youtube =['youtube','caută pe youtube','gaseste pe youtube']

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
            print('ati incercat sa spuneti: {}'.format(text))
        except sr.RequestError:
            print("Problema cu API-ul")
        except sr.UnknownValueError:
            print("Vocea nu a putut fi inteleasa...")

    return text

###youtube search###
def cauta_youtube(r):
    raspuns("Ce anume?")
    cautare = recunoastere_vocala(r)
    titlu = str(cautare).replace(" ","+")
    webbrowser.open('https://www.youtube.com/results?search_query={}'.format(titlu))

def cauta_google(r):
    raspuns("Ce anume?")
    print("Ce sa caut pe Google?")
    comanda =recunoastere_vocala(r)
    titlu = str(comanda).lower().replace(" ", "+")
    link = "https://www.google.com/search?client=opera-gx&q=titlul&sourceid=opera&ie=UTF-8&oe=UTF-8".replace("titlul",titlu)
    webbrowser.open(link)

def cauta_comanda(comanda):
    for i in dictionar_youtube:
        comanda_gasita=str(comanda).lower() == i.lower()
        if comanda_gasita:
            cauta_youtube(r)

    for i in dictionar_google:
        comanda_gasita = str(comanda).lower() == i.lower()
        if comanda_gasita:
            cauta_google(r)

def asculta_numele(r):
    while True:
        comanda = recunoastere_vocala(r)
        voce = str(comanda)
        index = voce.find("asistent")
        if index != -1:
            preia_comanda(r)
            break

def preia_comanda(r):
    raspuns("Da aici, gata sa te ajut!")
    comanda = recunoastere_vocala(r)
    cauta_comanda(comanda)

if __name__ == "__main__":
    r = sr.Recognizer()
    asculta_numele(r)


