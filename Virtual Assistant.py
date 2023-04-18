import pyttsx3 
import os
from tkinter import *
import speech_recognition as sr 
import webbrowser   
import datetime   
import subprocess
from PIL import ImageTk, Image

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        lisvar.set("Listening...")
        tkWindow.update()
        r.pause_threshold = 0.7
        audio = r.listen(source) 
        try: 
            lisvar.set("Recognizing...")
            tkWindow.update()
            Query = r.recognize_google(audio, language='en-in') 
            print("the command is printed=", Query) 
            lisvar.set("")

        except Exception as e: 
            print(e) 
            lisvar.set("can you repeat that")
            return "None"
        return Query 


def speak(audio):
    engine.say(audio)   
    engine.runAndWait() 


def tellDay(): 
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',  
                3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 
                7: 'Sunday'} 

      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week) 

  
def tellTime():  
    time = str(datetime.datetime.now()) 
    hour = time[11:13] 
    min = time[14:16] 
    speak( "The time is" + hour + "Hours and" + min + "Minutes")     

  
def Take_query(): 

    query = takeCommand().lower() 
    if "open drive" in query: 
        speak("Opening Drive ") 
        webbrowser.open("http://gdrivephp.epizy.com/") 

    elif "open google" in query: 
        speak("Opening Google ") 
        webbrowser.open("www.google.com") 

    elif 'open youtube' in query:
	    speak("Here you go to Youtube")
	    webbrowser.open("https://www.youtube.com/")

    elif "which day it is" in query: 
        tellDay() 

    elif 'open stack overflow' in query:
	    speak("Here you go to Stack Over flow.Happy coding")
	    webbrowser.open("https://stackoverflow.com/")

    elif 'shutdown system' in query:
	    speak("The system is shutting down")
	    subprocess.call('shutdown / p /f')

    elif "restart" in query:
        speak("The system is restarting")
        subprocess.call(["shutdown", "/r"])
    
    elif "hibernate" in query or "sleep" in query:
	    speak("The system is on sleep")
	    subprocess.call("shutdown / h")

    elif "tell me the time" in query: 
        tellTime() 

    elif "exit" in query: 
        speak("Good bye") 
        exit() 
     
    elif "tell me your name" in query: 
        speak("I am Your deskstop Assistant") 

  
if __name__ == '__main__': 
    tkWindow = Tk()  
    tkWindow.title("Virtual Assistant")
    tkWindow.wm_iconbitmap("micicon1.ico")
    tkWindow.geometry('500x600')  
    f1 = Frame(tkWindow,bg='#B5b1b1') #  #B5B1B1
    image = Image.open('Mic.png')
    image = image.resize((210,200),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image)
    lisvar = StringVar()
    lis = Label(f1,textvariable=lisvar,font="Century 18 normal",bg='#B5b1b1')
    lisvar.set("Welcome")
    lis.place(x=150,y=300,width="200",height=40)
    button = Button(f1,image=img1,bg='#B5b1b1',border='0',cursor='hand2',command = Take_query)  
    button.place(x=220,y=50,width="250",height=230)
    button.pack()
    f1.place(x=0, y=0, width=500, height=600)
    tkWindow.resizable(0, 0)
    tkWindow.mainloop()


