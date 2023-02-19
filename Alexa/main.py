import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('hello there, im your assistant ichigo')
engine.say('how can i help you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ichigo' in command:
                command = command.replace('ichigo', '')
                print(command)
    except:
        pass
    return command




def run_alexa():
    command = take_command()
    print(command)


    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'thank you' in command:
        talk('your most welcome')

    elif 'hello' in command:
        talk('hello, how can i assist you')

    elif 'hey' in command:
        talk('hey, do you need something')    

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'bye bye' in command:
        talk('goodbye, have a good day, take care')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    else:
        talk('Please say the command again.')



while True:
    run_alexa()