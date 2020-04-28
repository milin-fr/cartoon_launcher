import speech_recognition as sr
from pynput.mouse import Button, Controller

mouse = Controller()
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        if "next" in r.recognize_google(audio):
            mouse.position = (3354, 241)
            mouse.click(Button.left, 1)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
