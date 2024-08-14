import pygame
import os
import platform
import eel
import subprocess
from engine.config import *
from engine.voiceengine import *


@eel.expose
def playassistantsound():
    
    pygame.mixer.init()
    pygame.mixer.music.load('www/assets/audio/start_sound.mp3')
    
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# playassistantsound()

def opencommand(userquery):
    userquery = userquery.replace(Assistantname, "")
    userquery = userquery.replace("open", "")
    userquery = userquery.strip().lower()
    print(userquery)
    if userquery:
        say(f'Opening {userquery}')
        try:
            subprocess.Popen(userquery)
            print(userquery)
        except Exception as e:
            # say(f"Cannot open {userquery}. Error: {str(e)}")
            print(f'cant open {userquery}')
    else:
        say("Cannot open the app")
        print("Cant open jkdsfskdj")

