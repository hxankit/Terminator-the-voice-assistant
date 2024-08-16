import os
import eel
import platform
import socket
import subprocess

from engine.command import *
from engine.features import *
from engine.voiceengine import *
def start():  
    # say("welcome to here this is a code block ")
    playassistantsound()

    def find_free_port():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 0))
        port = sock.getsockname()[1]
        sock.close()
        return port

    # Set FONTCONFIG_PATH if it's not set
    if 'FONTCONFIG_PATH' not in os.environ:
        os.environ['FONTCONFIG_PATH'] = '/etc/fonts'

    # Initialize Eel
    eel.init("www")

    # Find a free port
    port = find_free_port()

    # Determine the operating system and set the appropriate command
    if platform.system() == 'Windows':
        browser_command = f'start chrome --app="http://localhost:{port}/index.html"'
    elif platform.system() == 'Linux':
        browser_command = f'google-chrome --app="http://localhost:{port}/index.html"'
    else:
        raise Exception("Unsupported operating system")
    # Start the Eel application
    try:
        # Start the browser with the appropriate command
        if platform.system() == 'Windows':
            os.system(browser_command)
        elif platform.system() == 'Linux':
            subprocess.Popen(browser_command, shell=True)

        # Start the Eel server
        eel.start('index.html', mode=None, host='localhost', port=port, block=True)
    except Exception as e:
        print(f"Error starting Eel server or browser: {e}")


