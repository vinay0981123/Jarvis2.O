from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
from JarvisAI import speak
from JarvisAI import takeCommand
def wtspmsg(name):
    msg1 = takeCommand().lower()
    print(msg1)
    speak(f"sending message to {name}")
    startfile("C:\\Users\\Vinay\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(12)
    click(x=266, y=108)
    sleep(1)
    write(name)
    sleep(1)
    click(x=275, y=239)
    sleep(1)
    click(x=647, y=697)
    sleep(1)
    write(msg1)
    press('enter')
def callTele(name):
    startfile("C:\\Users\\Vinay\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
    speak(f"calling{name}")
    sleep(1)
    click(x=216, y=46)
    sleep(0.5)
    write(name)
    sleep(1)
    click(x=240, y=95)
    sleep(1)
    click(x=1264, y=43)