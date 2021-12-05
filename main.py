from googlesearch import search
import speech_recognition as sr
from gtts import gTTS
from time import sleep
import os
import pyglet
import webbrowser
from bs4 import BeautifulSoup
import urllib


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
def cauta_youtube(r):
    raspuns("Ce sa caut pe youtube?")
    cautare = recunoastere_vocala(r)
    titlu = str(cautare).replace(" ","+")
    webbrowser.open('https://www.youtube.com/results?search_query={}]'.format(titlu))

def cauta_google(r):
    raspuns("Ce sa caut pe google?")
    print("Ce sa caut pe google?")
    comanda =recunoastere_vocala(r)
    titlu = str(comanda).lower()
    for url in search(titlu, stop=3):
        webbrowser.open(url)

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text



if __name__ == "__main__":
    r = sr.Recognizer()
    comanda = recunoastere_vocala(r)
    dictionar_comenzi = ['cauta pe youtube','google','notificari']
    print(str(comanda))
    if str(comanda).lower() == 'Caută pe YouTube'.lower():
        cauta_youtube(r)
    if str(comanda).lower() == "caută pe google".lower():
        cauta_google(r)