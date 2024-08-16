
import speech_recognition as sr
from engine.features import *
from engine.voiceengine import *
import eel
import time





manual_query ="play chandigrah song on youtube"



import speech_recognition as sr

def take_command():
    global current_language
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        # Adjust for ambient noise if needed
        r.adjust_for_ambient_noise(source)
        try:

            audio = r.listen(source, timeout=8, phrase_time_limit=6)
            print("Recognizing...")
            eel.DisplayMessage("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")

            # Optionally, you can perform further processing on the query here
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
            eel.DisplayMessage("Sorry, I did not understand the audio.")
            return ""  # Return empty string if speech could not be understood
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            eel.DisplayMessage("Sorry, there was an error with the speech recognition service.")
            return ""  # Return empty string if there was a request error
        except Exception as e:
            print(f"An error occurred: {e}")
            eel.DisplayMessage(f"An error occurred: {e}")
            return ""  # Return empty string for any other exceptions

@eel.expose
def allCommands(message=1):
    if message == 1:
        userquery=take_command()
    
        print(userquery)
    else:
        userquery= message

    
    
    if userquery != "":
            
        print(f'this is a query {userquery}')

        if "open".lower() in userquery.lower():
            print("Open comaand fired")
            openCommand(userquery);
        elif "play":
            playYtCommand(userquery)
        else:
            say("Sorry I cant open app")



    else:
        eel.ShowHood()
    
    eel.ShowHood()
        