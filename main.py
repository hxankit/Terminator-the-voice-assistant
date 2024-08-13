import os
import eel
import platform

eel.init("www")

# Determine the operating system and set the appropriate command
if platform.system() == 'Windows':
    # For Windows, using Google Chrome in app mode
    browser_command = 'start chrome --app="http://localhost:8000/index.html"'
elif platform.system() == 'Linux':
    # For Linux, using Google Chrome in app mode
    browser_command = 'google-chrome --app="http://localhost:8000/index.html"'
else:
    raise Exception("Unsupported operating system")

# Start the browser with the appropriate command
os.system(browser_command)

# Start the Eel application
eel.start('index.html', mode=None, host='localhost', port=8000, block=True)
