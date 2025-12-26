import datetime
import wikipedia
import streamlit as st
from gtts import gTTS
import os

# -----------------------------
# Function to "speak" text
# -----------------------------
def speak(text, use_audio=False):
    if use_audio:
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")
        audio_file = open("temp.mp3", "rb")
        st.audio(audio_file.read(), format='audio/mp3')
        audio_file.close()
        os.remove("temp.mp3")
    else:
        st.write(f"🗣️ {text}")

# -----------------------------
# Greeting based on time
# -----------------------------
def wishings(use_audio=False):
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning madam", use_audio)
    elif 12 <= hour < 17:
        speak("Good afternoon madam", use_audio)
    elif 17 <= hour < 21:
        speak("Good evening madam", use_audio)
    else:
        speak("Good night madam", use_audio)

# -----------------------------
# Get command from user
# -----------------------------
def commands():
    command = st.text_input("💬 Type your command", key="command_input")
    return command.lower() if command else ""

# -----------------------------
# Main app logic
# -----------------------------
if __name__ == "__main__":
    st.title("🦾 Jarvis AI Assistant")
    use_audio = st.checkbox("Enable voice output", value=False)
    
    # Greet user
    wishings(use_audio)
    
    # Get command
    query = commands()
    
    if query:
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}", use_audio)
        
        elif "wikipedia" in query:
            speak("Searching in Wikipedia...", use_audio)
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak(f"According to Wikipedia: {results}", use_audio)
            except:
                speak("No results found.", use_audio)
