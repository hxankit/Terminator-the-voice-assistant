import pygame
import os
import platform
import re
import webbrowser
import eel
import sqlite3
import subprocess
from engine.config import *
import pywhatkit as kit
from engine.db import *
from engine.voiceengine import *


@eel.expose
def playassistantsound():
    
    pygame.mixer.init()
    pygame.mixer.music.load('www/assets/audio/start_sound.mp3')
    
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# playassistantsound()

def openCommand(userquery):
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
                file_path = results[0][0]
                try:
                    subprocess.run(['xdg-open', file_path], check=True)
                except subprocess.CalledProcessError as e:
                    say(f"Error opening file: {e}")

            else:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    say("Opening " + userquery)
                    webbrowser.open(results[0][0])

                else:
                    say("Could not find the application or file. Attempting to open with subprocess.")
                    try:
                        subprocess.run(userquery, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        say(f"Error opening application: {e}")

        except Exception as e:
            say(f"Something went wrong: {e}")

# def PlayYoutube(userquery):
#     search_term = extract_yt_term(userquery)
#     say("Playing "+search_term+" on YouTube")
#     kit.playonyt(search_term)
def PlayYoutube(userquery):
    # Extract the search term from the user query
    search_term = extract_yt_term(userquery)
    
    # Check if the search term is None or an empty string
    if not search_term:
        search_term = "default search term"  # Use a default value or handle the error as needed
        say("No search term provided. Playing default video on YouTube.")
    else:
        say("Playing " + search_term + " on YouTube")
    
    # Play the video on YouTube
    kit.playonyt(search_term)


def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None



