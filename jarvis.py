import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Corrected 'voices' to 'voice'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():  # Takes input from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        print("Wait for a few seconds... ")
        query = r.recognize_google(audio, language="en-in")  # Changed to recognize_google
        print(f"You just said: {query}\n")
    except Exception as e:  # e is used to store the type of error
        print(e)
        speak("Please tell me again...")
        query = "none"
    return query

# Get the command from the user
def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        print("good morning madam")
        speak("good morning madam")
    elif hour >=12 and hour <17:
        print("good afternoon  madam")
        speak("good afternoon madam")
    elif hour >=17 and hour <21:
        print("good evening madam")
        speak("good evening madam")
    else:
        print("good night madam")
        speak("good night madam")

if __name__ == "__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"The time is {strTime}")

    elif 'open firefox' in query:
        speak("opening firefox application madam")
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    elif 'wikipeda' in query:
        speak("searching in wikipedia")
        try:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 1)
            speak("acoording to wikipedia,")
            print(results)
            speak(results)
        except:
            speak("no results found..")
            print("no results found..")
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Corrected 'voices' to 'voice'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():  # Takes input from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        print("Wait for a few seconds... ")
        query = r.recognize_google(audio, language="en-in")  # Changed to recognize_google
        print(f"You just said: {query}\n")
    except Exception as e:  # e is used to store the type of error
        print(e)
        speak("Please tell me again...")
        query = "none"
    return query

# Get the command from the user
def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        print("good morning madam")
        speak("good morning madam")
    elif hour >=12 and hour <17:
        print("good afternoon  madam")
        speak("good afternoon madam")
    elif hour >=17 and hour <21:
        print("good evening madam")
        speak("good evening madam")
    else:
        print("good night madam")
        speak("good night madam")

if __name__ == "__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"The time is {strTime}")

    elif 'open firefox' in query:
        speak("opening firefox application madam")
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    elif 'wikipeda' in query:
        speak("searching in wikipedia")
        try:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 1)
            speak("acoording to wikipedia,")
            print(results)
            speak(results)
        except:
            speak("no results found..")
            print("no results found..")