import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os


engine = pyttsx3.init()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("current time is")
    speak(Time)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("today's date is")
    speak(day)
    speak(month)
    speak(year)


def wishMe():
    speak("Welcome back sir!")
    speak("How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en')
        print(query)
    except Exception as e:
        print(e)
        speak("unable to hear you, please try again")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("searching..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'browser search' in query:
            speak("what should I search?")
            chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromePath).open_new_tab(search + '.com')

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /r /t 1")

        elif 'bye' in query:
            quit()
