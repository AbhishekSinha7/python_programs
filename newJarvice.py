from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime

root = Tk()
root.title("Virtual Assistant in Python")

global user_said_label
global listeningvar
user_said_label = StringVar()
listeningvar = StringVar()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        listeningvar.set("Good Morning Sir!")
        root.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        listeningvar.set("Good Afternoon Sir!")
        root.update()
        speak("Good Afternoon Sir!")
    else:
        listeningvar.set("Good Evening Sir!")
        root.update()
        speak("Good Evening Sir!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    """ It takes microphone input from the user and return string output """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        listeningvar.set("Listening...")
        root.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        listeningvar.set("Recognizing...")
        root.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")

    except Exception as e:
        # print(e)
        listeningvar.set("Say that again please...")
        root.update()
        speak("Say that again please...")
        # print("Network Error...")
        # print("Say that again please...")

        return "None"
    user_said_label.set(query)
    root.update()
    return query


def play_mic():
    wishme()
    while True:
        query = takeCommand().lower()
        if "exit" in query:
            listeningvar.set("Bye sir!")
            root.update()
            speak("Bye sir")
            break

        elif "open geeksforgeeks" in query:
            listeningvar.set("Opening geeksforgeeks")
            root.update()
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")


        elif "open google" in query:
            listeningvar.set("Opening google")
            root.update()
            speak("Opening Google ")
            webbrowser.open("www.google.com")


        elif "bye" in query:
            listeningvar.set("Bye Sir!")
            root.update()
            speak("Bye sir!")
            exit()

        elif "hello" in query:
            listeningvar.set("Hello Sir!")
            root.update()
            speak("Hello Sir!")


        elif "wikipedia" in query:
            if "open wikipedia" in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("Checking the wikipedia ")
                    query = query.replace("according to wikipedia", "")
                    result = wikipedia.summary(query, sentences=4)
                    speak("According to wikipedia")
                    listeningvar.set(result)
                    root.update()
                    speak(result)
                except Exception as e:
                    user_said_label.set("Sorry sir could not find any results")
                    root.update()
                    speak("Sorry sir could not find any results")


        elif "tell me your name" in query:
            listeningvar.set("I am Jarvis. Your deskstop Assistant!")
            root.update()
            speak("I am Jarvis. Your deskstop Assistant")


def quitfun():
    exit()

f1 = Frame(root) #  #B5B1B1 bg='#B5b1b1'

image = Image.open('Mic.png')
image = image.resize((210,200),Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(image)


userlabel = Label(f1,textvariable=user_said_label,font="Century 14 normal")
user_said_label.set("Used Said:")
userlabel.place(x=20,y=20,width="100",height=40)


labelmain = Label(f1,textvariable=listeningvar,font="Century 18 normal")
listeningvar.set("Welcome")
labelmain.place(x=120,y=70,width="250",height=40)

button = Button(f1,image=img1,border='0',cursor='hand2',command=play_mic)
button.place(x=125,y=150,width=250,height=230)

quitbtn = Button(f1,text="Quit",border='0',bg="orange",cursor='hand2',command=quitfun)
quitbtn.place(x=375,y=400,width=100,height=40)

f1.place(x=0,y=0,width=500,height=500)

root.resizable(0, 0)
root.geometry("500x500")
root.mainloop()
