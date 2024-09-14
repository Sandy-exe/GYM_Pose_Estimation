import pyttsx3

engine = pyttsx3.init()

def speak(text):
    if not engine._inLoop:
        engine.say(text)
        engine.runAndWait()
    else:
        engine.say(text)
