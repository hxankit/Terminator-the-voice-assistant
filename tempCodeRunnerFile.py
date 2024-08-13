import os 
import eel

eel.init("www")
# os.system('start msedge.exe --app=="http://localhost:8000/index.html ')
os.system('start firefox --app=="http://localhost:9000/index.html ')

eel.start('index.html',mode=None,host='localhost', block=True)