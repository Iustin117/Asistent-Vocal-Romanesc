import warnings
import speech_recognition as sr
from gtts import gTTS
from time import sleep
import os
import pyglet
import webbrowser
import YouTubeSearchAVR
import whatsappAVR
import Agenda


warnings.filterwarnings("ignore")

###dictionare
dictionar_google = ['google', 'caută pe google', 'gaseste pe google', 'caută ceva pentru mine', 'caută', "spune și mie"]
dictionar_youtube =['youtube', 'caută pe youtube', 'gaseste pe youtube']
dictionar_youtube_play =['play', 'pune melodia', 'pune videoclipul', 'caută videoclipul', 'caută melodia']
dictionar_whatsap = ['whatsapp', 'trimite un mesaj', 'trimite un mesaj pe whatsapp', 'mesaj']
dictionar_positiv = ['da', 'da asta e', 'da e corect', 'corect', 'da este corect', 'perfect', 'da este']
dictionar_negativ = ['nu', 'nu este', 'nu e', 'nu e corect', 'nu este corect', 'gresit']
dictionar_iesire = ['iesi', 'nu am nevoie de nimic', 'nu mai am nevoie de nimic', 'nu mulțumesc']
dictionar_agenda_adauga_contact = ['agendă', 'deschide agendă', 'contacte']

###Raspuns###
def raspuns(text):
    tts = gTTS(text=text, lang='ro')
    filename = 'temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration)
    os.remove(filename)

####Recunoastere vocala####
def recunoastere_vocala():
    while True:
        with sr.Microphone() as source:
            print("Spune orice:")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="ro-RO")
                print('ati incercat sa spuneti: {}'.format(text))
                return text
            except sr.RequestError:
                print("Problema cu API-ul")
            except sr.UnknownValueError:
                print("Vocea nu a putut fi inteleasa...")

def cauta_youtube():
    raspuns("Ce anume?")
    cautare = recunoastere_vocala()
    titlu = str(cautare).replace(" ", "+")
    link = 'https://www.youtube.com/results?search_query={}'.format(titlu)
    webbrowser.open(link)

def cauta_google():
    raspuns("Ce anume?")
    print("Ce sa caut pe Google?")
    comanda = recunoastere_vocala()
    titlu = str(comanda).lower().replace(" ", "+")
    link = "https://www.google.com/search?client=opera-gx&q=titlul&sourceid=opera&ie=UTF-8&oe=UTF-8".replace("titlul", titlu)
    webbrowser.open(link)

def youtube_play():
    raspuns("Ce anume?")
    cautare = recunoastere_vocala()
    titlu = str(cautare).replace(" ", "+")
    YouTubeSearchAVR.youtube_play(titlu)

def cauta_comanda(comanda):
    for i in dictionar_youtube:
        comanda_gasita= str(comanda).lower() == i.lower()
        if comanda_gasita:
            cauta_youtube()

    for i in dictionar_google:
        comanda_gasita = str(comanda).lower() == i.lower()
        if comanda_gasita:
            cauta_google()

    for i in dictionar_youtube_play:
        comanda_gasita = str(comanda).lower() == i.lower()
        if comanda_gasita:
            youtube_play()

    for i in dictionar_whatsap:
        comanda_gasita = str(comanda).lower() == i.lower()
        if comanda_gasita:
            whatapp_get_info()
    for i in dictionar_agenda_adauga_contact:
        comanda_gasita = str(comanda).lower() == i.lower()
        if comanda_gasita:
            adauga_contact()

def asculta_numele():
    while True:
        comanda = recunoastere_vocala()
        voce = str(comanda)
        index = voce.find("asistent")
        if index != -1:
            preia_comanda()
            break

def preia_comanda():
    raspuns("Da?")
    comanda = recunoastere_vocala()
    cauta_comanda(comanda)

def whatapp_get_info():
    global numar, mesaj
    raspuns("Cui vrei să trimiți un mesaj? Poți sî imi spui numarul de telefon?")
    nr_corect =False
    while nr_corect == False:
        raspuns("repeta numarul")
        nr_corect = True
        numar = str(recunoastere_vocala()).replace(" ", "")
        raspuns(str(numar)+" este corect?")
        corect = recunoastere_vocala()
        nr_corect = verifica(corect)
    raspuns("Perfect, acum ce mesaj vrei sa primeasca?")
    mesaj_corect = False
    while mesaj_corect == False:
        raspuns("Repeta mesajul:")
        mesaj_corect = True
        mesaj = recunoastere_vocala()
        raspuns(str(mesaj)+" este corect?")
        corect = recunoastere_vocala()
        mesaj_corect = verifica(corect)
    whatsappAVR.whatsap_trimite_mesaj(numar, mesaj)

def verifica(com):
    for i in dictionar_positiv:
        positiv = str(com).lower() == i.lower()
        if positiv:
            return positiv
    for i in dictionar_negativ:
        negativ = str(com).lower == i.lower()
        if negativ:
            positiv = False
            return  positiv

def adauga_contact():
    raspuns("Pe cine vrei să adaugi in agenda?")
    nume = recunoastere_vocala()
    raspuns(nume+" Este corect?")
    confirmare = recunoastere_vocala()
    if verifica(confirmare):
        Agenda.adauga_nume(nume)
    else:
        nume_corect = False
        while nume_corect == False:
            nume_corect = True
            raspuns("Atunci repetă numele")
            nume = recunoastere_vocala()
            raspuns(nume + " Este corect?")
            corectie = recunoastere_vocala()
            nume_corect = verifica(corectie)
        Agenda.adauga_nume(nume)


    raspuns("Numarul de telefon?")
    nr = recunoastere_vocala()
    confirmare = recunoastere_vocala()
    if verifica(confirmare):
        Agenda.adauga_numar(nr)
    else:
        nr_corect = False
        while nr_corect == False:
            nr_corect = True
            raspuns("Atunci repetă numele")
            nr = recunoastere_vocala()
            raspuns(nr + " Este corect?")
            corectie = recunoastere_vocala()
            nr_corect = verifica(corectie)
        Agenda.adauga_nume(nr)


if __name__ == "__main__":
    r = sr.Recognizer()
    while True:
        asculta_numele()