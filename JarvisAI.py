import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import time
# initializing or creating object
engine = pyttsx3.init("sapi5")
# voices will contain voices like in this system there is 3 type of voice
voices = engine.getProperty("voices")
# print(voices)
# here we are choosing a voice or setting voice
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("good evening sir")
    speak("I am Jarvis Sir. Please tell me how may i help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print("Listening...")
        r.energy_threshold = 400
        # r.pause_threshold=1
        audio = r.listen(source)
    try:
        speak("Recognizing")
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")
    except Exception as e:
        print("say that again please")
        return "None"
    return query


def rNumber():
    return random.randint(0, 3)


def VideoDownloader():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep
    sleep(2)
    print("starting process..")
    click(x=503, y=50)
    hotkey('ctrl', 'x')
    value = pyperclip.paste()
    Link = str(value)
    print(Link)

    def Download(link):
        speak("starting download")
        url = YouTube(link)
        video = url.streams.first()
        video.download("C:\\Users\\Vinay\\Desktop\\Jarvis\\Downloads")
    Download(Link)
    speak("Done sir, I am successfully downloaded this video")
    speak("let me show you the file")
    os.startfile("C:\\Users\\Vinay\\Desktop\\Jarvis\\Downloads")


def YouTubeSearch(term):
    result = f"https://www.youtube.com/results?search_query={term}"
    webbrowser.open(result)
    speak("this is what i found for you sir")
    time.sleep(5)
    pywhatkit.playonyt(term)
    speak("this may also help you sir.")