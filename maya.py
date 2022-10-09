from random import random
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
num = random.randint(1, 92)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Hello and Good Morning Sir!")
        speak("Hello and Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        print("Hello and Good Afternoon Sir!")
        speak("Hello and Good Afternoon Sir!")
    else:
        print("Hello and Good Evening Sir!")
        speak("Hello and Good Evening Sir!")

    print("I am Maya. Please tell me how can I help you?")
    speak("I am Maya sir. Please tell me how can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while (True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, 2)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'D:\\My File\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'time' in query:
            srtTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {srtTime}")
            speak(f"The time is {srtTime}")
