import datetime

import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit



listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice','french')

def parler(text):
    engine.say(text)
    engine.runAndWait()
def ecouter():

    try:
        with sr.Microphone() as source:
            print("Parlez maintenant s'il vous plait !!")
            voix = listener.listen(source)
            command = listener.recognize_google(voix)
            command.lower()
    except:
        pass
    return command


def lancer_assistant():
    command = ecouter()
    print(command)
    if 'put on the song ' in command:
        chanteur = command.replace('put on the song ','')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
        parler(chanteur)
    elif 'what time is it' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        parler('It is ' + heure)
    elif 'hello' in command:
        parler('hello Moataz')
    else:
        print('I do not understand')
        parler('I do not understand')

lancer_assistant()


while True:
    lancer_assistant()
