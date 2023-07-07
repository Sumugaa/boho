import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os
import pyjokes
import pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("hello this is Boho reporting")

def tellday():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4:'Thursday', 5: 'Friday', 6:'Saturday', 7: 'Sunday'}
    if day in day_dict.keys():
        dotw = day_dict[day]
        print(dotw)
        speak("Today is "+dotw)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said- {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query

def funcs():
    k=0
    while k==0:
        query = takeCommand().lower()
        if 'bye' not in query:
            if 'google' in query:
                query=query.replace("google", "")
                pywhatkit.search(query)
            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak("According to wikipedia, ")
                print(results)
                speak(results)
            elif 'youtube' in query:
                webbrowser.open("www.youtube.com")
            elif 'stack overflow' in query:
                webbrowser.open("www.stackoverflow.com")
            elif 'gmail' in query:
                webbrowser.open("www.gmail.com")
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif 'notepad' in query:
                codePath = "notepad.exe"
                os.startfile(codePath)
            elif 'joke' in query:
                speak(pyjokes.get_joke('en','neutral'))
                print(pyjokes.get_joke('en','neutral'))
            elif 'day' and 'today' in query:
                tellday()
            elif 'powerpoint' in query:
                codePath = "POWERPNT.EXE"
                os.startfile(codePath)
            elif 'ms word' in query:
                codePath = "WINWORD.EXE"
                os.startfile(codePath)
            elif 'date' in query:
                date = datetime.datetime.now().strftime("%D: %m: %y")
                speak(f"The date is {date}")
            elif 'play' in query:
                song=query.replace("play","")
                speak("Playing "+song)
                pywhatkit.playonyt(song)
            elif 'spotify' in query:
                codePath = "C:\\Users\\sumug\\AppData\\Roaming\\Spotify\\Spotify.exe"
                os.startfile(codePath)
            
        else:
            print("It was a pleasure. Until next time..")
            speak("It was a pleasure. Until next time..")
            k=1
            #return "none"

funcs()
            