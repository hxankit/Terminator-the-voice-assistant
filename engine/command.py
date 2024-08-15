
import speech_recognition as sr
from engine.features import *
from engine.voiceengine import *
import eel
import time









def take_command():
    global current_language  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening...")
        eel.DisplayMessage("Listening...")
        # eel.ShowHood()
        audio = r.listen(source,8,6)

        try:
            print("Recognizing...")
            eel.DisplayMessage("Recognizing...")
            query = r.recognize_google(audio, language=current_language)
            print(f"User said: {query}")
            
            time.sleep(3)
            # say(query)
            return query.lower()
        except Exception as e:
            return ""
        return query.lower()

@eel.expose
def allCommands():
    
    userquery=take_command()
    
    # say(userquery)
    print(userquery)
    if "open".lower() in userquery.lower():
        openCommand(userquery);
    elif "on youtube":
        PlayYoutube(userquery);
    else:
        say("Sorry I cant open app")



    eel.ShowHood()