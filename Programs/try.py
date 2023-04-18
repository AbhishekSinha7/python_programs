import pyttsx3 

from tkinter import *

import speech_recognition as sr 

import webbrowser   

import datetime   

import wikipedia  

from PIL import ImageTk, Image

global lis
def takeCommand(): 

    r = sr.Recognizer() 

    with sr.Microphone() as source: 


        r.pause_threshold = 0.7

        audio = r.listen(source) 

          

        try: 


            Query = r.recognize_google(audio, language='en-in') 

            print("the command is printed=", Query) 

              

        except Exception as e: 

            print(e) 

            print("Say that again sir") 

            return "None"

          

        return Query 

  

def speak(audio): 

      
    engine = pyttsx3.init() 

    voices = engine.getProperty('voices') 

    engine.setProperty('voice', voices[0].id) 

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

    print(time) 

    hour = time[11:13] 

    min = time[14:16] 

    speak( "The time is sir" + hour + "Hours and" + min + "Minutes")     

  

def Hello(): 


    speak("hello sir I am your desktop assistant. Tell me how may I help you") 

  

  

def Take_query(): 

    Hello() 


    while(True): 


        query = takeCommand().lower() 

        if "open geeksforgeeks" in query: 

            speak("Opening GeeksforGeeks ") 

            webbrowser.open("www.geeksforgeeks.com") 


          

        elif "open google" in query: 

            speak("Opening Google ") 

            webbrowser.open("www.google.com") 


              

        elif "which day it is" in query: 

            tellDay() 


          

        elif "tell me the time" in query: 

            tellTime() 


          
        elif "bye" in query: 

            speak("Bye. Check Out GFG for more exicting things") 

            exit() 

          

        elif "from wikipedia" in query: 

            speak("Checking the wikipedia ") 

            query = query.replace("wikipedia", "") 

            result = wikipedia.summary(query, sentences=4) 

            speak("According to wikipedia") 

            speak(result) 

          

        elif "tell me your name" in query: 

            speak("I am Jarvis. Your deskstop Assistant") 

  

if __name__ == '__main__': 

    tkWindow = Tk()  
    
    tkWindow.title("Virtual Assistant")
   # tkWindow.wm_iconbitmap("micicon1.ico")
    tkWindow.geometry('500x700')  
    f1 = Frame(tkWindow,bg='#B5b1b1') #  #B5B1B1
    image = Image.open('E:\python\Programs\Mic.png')
    image = image.resize((210,200),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image)

    tkWindow.resizable(0,0)

    '''buttonmic = Button(f1,image=img1,bg='#B5b1b1',border='0',cursor='hand2')
    buttonmic.place(x=220,y=50,width="250",height=230)
    buttonmic.bind("<ButtonPress>", speakfun)
'''
    lis = Label(f1,text="kaamchor...",font="Century 18 normal",bg='#B5b1b1')
    lis.place(x=150,y=300,width="200",height=40)
    f1.place(x=0,y=0,width="500",height=700)

    button = Button(f1,image=img1,bg='#B5b1b1',border='0',cursor='hand2',command = Take_query)  
    button.place(x=220,y=50,width="250",height=230)
    button.pack()  

    tkWindow.mainloop()

