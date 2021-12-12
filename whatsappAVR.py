import pywhatkit
from datetime import datetime

def whatsap_trimite_mesaj(number, mesaj):#https://web.whatsapp.com/send?phone="phone_number_with_prefix"&text="mesaj"%
    now = datetime.now()
    curent_time = now.strftime("%H:%M:%S")
    time_to_int = [int(curent_time[0:2]), int(curent_time[3:5]), int(curent_time[6:8])]
    ora = time_to_int[0]
    minutul = time_to_int[1] + 1
    secunda = 10
    number = "+4"+number
    pywhatkit.sendwhatmsg(number, mesaj, ora, minutul, secunda, True, 10)

