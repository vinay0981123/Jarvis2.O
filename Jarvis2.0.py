from JarvisAI import takeCommand
from JarvisAI import speak
from JarvisAI import wish_me
from JarvisAI import rNumber
from JarvisAI import YouTubeSearch
from pyautogui import hotkey
from Automation import wtspmsg
from Automation import callTele
import pywhatkit
import time
import pyautogui
import wikipedia
import webbrowser
import os
import datetime
from JarvisAI import YouTubeSearch
if __name__ == "__main__":
    wish_me()
    while True:
        query=takeCommand().lower()
        # query="whatsapp"
        
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("who is", "")
            query = query.replace("according to", "")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "search on google" in query:
            import wikipedia as googleScrap
            speak("what have to search sir")
            search = takeCommand().lower()
            pywhatkit.search(search)
            speak("this is what i found sir")
            try:
                result = googleScrap.summary(query, 3)
                speak(result)
            except:
                speak("no speakable data available")
        elif "my website" in query:
            speak("opening your website")
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s")
            webbrowser.open_new("https://explorecode098.blogspot.com/")
            
        elif "play music" in query:
            songs = os.listdir(r"D:\songs")
            print(songs)
            i = rNumber()
            os.startfile(f"D:/songs/{songs[i]}")

            while True:
                changeq = takeCommand().lower()
                print(changeq)
                if "change" in changeq:
                    speak("OK sir. Changing music")
                    i = rNumber()
                    os.startfile(f"D:/songs/{songs[i]}")
                elif "stop" in changeq:
                    hotkey('alt', 'f4')
                    break
        elif "close" in query:
            hotkey('alt','f4')

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "search on youtube" in query:
            speak("what have to search sir")
            term = takeCommand().lower()
            
            term = term.replace("search", "")
            term = term.replace("jarvis", "")
            YouTubeSearch(term)
        elif "download" in query:
            from JarvisAI import VideoDownloader
            VideoDownloader()
        elif "whatsapp" in query:
            speak("to which person you want to send message.")
            name = takeCommand().lower()
            speak("what mesaage have to send sir")
            print(name)
            wtspmsg(name)
        
        elif "make a call" in query:
            speak("to which person you want to make call")
            name = takeCommand().lower()
            name = name.replace("to", "")
            callTele(name)
        elif "quit" in query:
            break