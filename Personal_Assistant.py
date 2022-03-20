import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hey Darshan, Jarvis here How can i help you")

def takecommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-in")
        print("user said:", query)
    except Exception as e:
        print(e)
        speak("'Say that agin please..")
        return "none"
    return query

if 1:
    # speak(Good boy)
    wishme(datetime)  

    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia....please wait for a while")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open notepad' in query:
            npath = 'C:\WINDOWS\system32\notepad.exe'
            os.startfile(npath)

        elif 'open command promt' in query:
            os.system('start cmd')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open calender' in query:
            webbrowser.open("calender.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%h:%m:%S")
            speak(f"The time is{strTime}")

        elif 'no thanks' in query:
            speak("Thank You, have a great day")
sys.exit()       

