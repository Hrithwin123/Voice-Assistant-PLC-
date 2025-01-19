import speech_recognition as sr
import pyttsx3 as ttsx
import webbrowser as wb
import pywhatkit as whatsapp
import sys
import pyautogui as gui
import pyperclip


from contacts import contactlist

recognizer = sr.Recognizer()
tts = ttsx.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

def commandlist(command):
    if("google" in command.lower()):
        wb.open("https://www.google.com/")
        speak("opening google")

    elif("gmail" in command.lower()):
        wb.open("https://www.gmail.com/")
        speak("opening gmail")
    
    elif("chat gpt" in command.lower()):
        wb.open("https://www.chatgpt.com/")
        speak("opening chat gpt")
    
    elif("whatsapp" in command.lower()):
        wb.open("https://web.whatsapp.com/")
        speak("opening whatsapp")
    
    elif("youtube" in command.lower()):
        wb.open("https://youtube.com/")
        speak("opening youtube")

    elif("message" in command.lower()):
        message = []
        check = False
        wordlist = command.split()
        for word in wordlist:

            if(check):
                message.append(word)
            if(word == "message"):
                check = True

        person = message[0]
        message = " ".join(message[1:])

        print(person)
        if(person.lower() in contactlist):
            print(contactlist[person.lower()])
            print(message)    
            whatsapp.sendwhatmsg_instantly(contactlist[person.lower()], message,7,True,1)
            speak(f"Message has been sent")
        else:
            print("Contact not found")
            speak("Contact not found")

    elif("search" in command.lower()):
        search = []
        check = False
        wordlist = command.split()
        for word in wordlist:
            if(check):
                search.append(word)
            if(word == "search"):
                check = True
        search = " ".join(search)
        whatsapp.search(search)
        speak(f"Searching {search}")
    
    elif("play video" in command.lower()):
        print("youtube searching")
        search = []
        check = False
        wordlist = command.split()
        for word in wordlist:
            if(check):
                search.append(word)
            if(word == "video"):
                check = True
        search = " ".join(search)
        whatsapp.playonyt(search)
        speak(f"Playing Video {search}")

    elif("word" in command.lower()):
        gui.click(612, 1044)
        speak("opening word")

    elif("excel" in command.lower()):
        gui.click(692, 1047)
        speak("opening excel")

    elif("powerpoint" in command.lower()):
        gui.click(764, 1052)
        speak("opening powerpoint")

    elif("copy text" in command.lower()):
        search = []
        check = False
        wordlist = command.split()
        for word in wordlist:
            if(check):
                search.append(word)
            if(word == "video"):
                check = True
        search = " ".join(search)
        pyperclip.copy(search)
        speak("Copied text")


    else:
        print("No command available")
    
            
def initialListen():
    with sr.Microphone() as source:
        while True:
            try:
                print("Listening....")
                audio = recognizer.listen(source, timeout = 1)
                speech = recognizer.recognize_google(audio)

                if("python" in speech.lower()):
                    break

                elif("exit" in speech.lower()):
                    speak("Python Shutting Down")
                    sys.exit(0)
                    
            except:
                print("Word wasnt recognisable")

        print("What would you like to do sir ??")
        speak("What would you like to do sir ??")
        commandlisten()

def commandlisten():
    with sr.Microphone() as source:
        while True:
            try : 
                command_speech = recognizer.listen(source)
                command = recognizer.recognize_google(command_speech)
                if("stop" in command.lower()):
                    speak("Python has stopped listening for commands")
                    initialListen()
                else:
                    commandlist(command)

            except : 
                print("Command wasnt recognisable")

initialListen()