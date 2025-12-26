import pyttsx3
import datetime
import os
import wikipedia

# Streamlit (for cloud)
import streamlit as st

# -----------------------------
# Optional Voice Support
# -----------------------------
try:
    import speech_recognition as sr
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False


# -----------------------------
# Text-to-Speech Engine
# -----------------------------
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Greeting Function
# -----------------------------
def wishings():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        msg = "Good morning"
    elif 12 <= hour < 17:
        msg = "Good afternoon"
    elif 17 <= hour < 21:
        msg = "Good evening"
    else:
        msg = "Good night"

    print(msg)
    speak(msg)


# -----------------------------
# Voice Command (Local only)
# -----------------------------
def voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Please say that again")
        return ""


# -----------------------------
# Command Processor
# -----------------------------
def process_command(query):
    if "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
        st.write(f"🕒 Time: {time}")

    elif "open firefox" in query:
        speak("Opening Firefox")
        os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")

    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=1)
            speak(result)
            st.write(result)
        except:
            speak("No results found")
            st.write("No results found")

    else:
        speak("Sorry, I didn't understand")
        st.write("❓ Command not recognized")


# =============================
# STREAMLIT APP
# =============================
st.title("🤖 Jarvis AI Assistant")

wishings()

if VOICE_AVAILABLE:
    if st.button("🎤 Use Voice Command"):
        command = voice_command()
        if command:
            process_command(command)
else:
    st.warning("🎤 Voice input not supported on Streamlit Cloud")

    command = st.text_input("💬 Type your command")
    if command:
        process_command(command.lower())
