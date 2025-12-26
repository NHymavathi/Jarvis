import datetime
import os
import wikipedia
import streamlit as st

def speak(text):
    # On Streamlit Cloud, just display text instead of speaking
    st.write(f"🗣️ {text}")

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning madam")
    elif hour >=12 and hour <17:
        speak("Good afternoon madam")
    elif hour >=17 and hour <21:
        speak("Good evening madam")
    else:
        speak("Good night madam")

def commands():
    command = st.text_input("💬 Type your command")
    return command.lower() if command else ""

if __name__ == "__main__":
    wishings()
    query = commands()
    if query:
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            try:
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=1)
                speak(f"According to Wikipedia: {results}")
            except:
                speak("No results found.")
from gtts import gTTS
import streamlit as st
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    audio_file = open("temp.mp3", "rb")
    st.audio(audio_file.read(), format='audio/mp3')
    import streamlit as st
import datetime
import wikipedia
import os

def speak(text):
    st.write(f"🗣️ {text}")  # just display text instead of speaking

def wishings():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning madam")
    elif hour < 17:
        speak("Good afternoon madam")
    elif hour < 21:
        speak("Good evening madam")
    else:
        speak("Good night madam")

def commands():
    command = st.text_input("💬 Type your command", key="command_input")
    return command.lower() if command else ""

if __name__ == "__main__":
    wishings()
    query = commands()
    if query:
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "wikipedia" in query:
            speak("Searching in Wikipedia...")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak(f"According to Wikipedia: {results}")
            except:
                speak("No results found.")


