import speech_recognition as sr

def test_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Could not understand audio")

test_microphone()
