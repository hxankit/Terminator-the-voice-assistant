import pyttsx3
import eel
current_language ="en-in"
engine = pyttsx3.init('espeak')
# Set properties for the TTS engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose a different index if this voice is unclear
engine.setProperty('rate', 150)  # Adjust the rate as needed




def say(text):
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


