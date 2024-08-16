import pygame
import os
import platform
import re
import webbrowser
import pvporcupine
import struct
import time
import xdotool as xdo
import pyaudio
import eel
import sqlite3
import subprocess
import pywhatkit as kit
from engine.config import *
from engine.db import cursor
from engine.voiceengine import *
from engine.helper import *


@eel.expose
def playassistantsound():
    
    pygame.mixer.init()
    pygame.mixer.music.load('www/assets/audio/start_sound.mp3')
    
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# playassistantsound()


def PlayYoutube(search_term):
    # Check if search_term is None
    if search_term is None:
        # Handle the case when search_term is None
        say("No search term provided.")
        return

    # Proceed with normal functionality if search_term is valid
    say("Playing " + search_term + " on YouTube")





def openCommand(userquery):
    # say("welcome in open")
    userquery = userquery.replace(Assistantname, "")
    userquery = userquery.replace("open", "")
    userquery = userquery.strip().lower()

    app_name = userquery

    if app_name != "":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                say("Opening " + userquery)
                print(results[0][0])
                file_path = results[0][0]
                try:
                    subprocess.run(['xdg-open', file_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error opening file: {e}")

            else:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    url = results[0][0]
                    say("Opening " + userquery)
                    try:
                        print(f"Attempting to open URL: {url}")  # Debugging line
                        webbrowser.get('firefox').open(url)
                    except Exception as e:
                        print(f"Error opening URL: {e}")

                else:
                    say("Could not find the application or file. Attempting to open with subprocess.")
                    try:
                        subprocess.run(userquery, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        say(f"Error opening application: {e}")

        except Exception as e:
            say(f"Something went wrong: {e}")

def PlayYoutube(userquery):
    # Extract the search term from the user query
    search_term = extract_yt_term(userquery)
    print(search_term)
    
    # Check if the search term is None or an empty string
   
    say("Playing " + search_term + " on YouTube")
    
    # Play the video on YouTube
    kit.playonyt(search_term)






def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Initialize Porcupine for keyword detection
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])
        
        # Initialize PyAudio for audio streaming
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        
        print("Listening for hotwords...")
        
        # Loop for streaming and processing audio
        while True:
            try:
                # Read audio data from the stream
                keyword = audio_stream.read(porcupine.frame_length)
                keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
                
                # Process the audio data to detect keywords
                keyword_index = porcupine.process(keyword)
                
                if keyword_index >= 0:

                    print("Hotword detected!")
                    # say("Hotword detected!")
                    print(keyword_index)
                    print(keyword)
                    # Simulate pressing the Super (Windows) key and 'j'
                    try:
                     # Simulate pressing the Super (Windows) key and 'j'
                        # time.sleep(3)  # Wait for 2 seconds
                        subprocess.run(['xte', 'keydown Super_L', 'key j', 'keyup Super_L'], check=True)
                        print("Key press simulated successfully.")
                    except subprocess.CalledProcessError as e:
                        print(f"Error with xte command: {e}")
                    except Exception as e:
                        print(f"Unexpected error: {e}")
                    time.sleep(2)
            
            except IOError as e:
                print(f"Audio error: {e}")
                break  # Exit loop on audio error
            except Exception as e:
                print(f"Unexpected error during audio processing: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Cleanup resources
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
