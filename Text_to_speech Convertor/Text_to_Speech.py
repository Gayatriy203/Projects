import pyttsx3
import tkinter
from tkinter import *
from tkinter.ttk import Combobox
import gtts
import os
from playsound import playsound


#tk window size
root = Tk()
root.geometry("720x600")
root.title("Text  to Speech Convertor")
root.config(bg='#CD69C9')

# function to convert
trans=pyttsx3.init()
def speaknow():
    text=text_box.get(1.0,END)
    gender=gender_box.get()
    speed=speed_box.get()
    voices=trans.getProperty("voices")
    
    def setvoice():
        if(gender == 'Male'):
            trans.setProperty('voices',voices[0].id)
            trans.say(text)
            trans.runAndWait()
        else:
            trans.setProperty('voices',voices[1].id)
            trans.say(text)
            trans.runAndWait()
    if(text):
        if(speed == 'Fast'):
            trans.setProperty("rate",250)
            setvoice()
        elif(speed == 'Medium'):
            trans.setProperty("rate",150)
            setvoice()
        else:
            trans.setProperty("rate",60)
            setvoice()
    n4 = gtts(text=trans, slow=False)
    n4.save("Text_to_speech.mp3")
#lable to tkwindow
Label(root,text="  Text To Speech Convertor  ",font="arial 40 bold",bg="BLACK",fg="#FF83FA").place(x=0,y=0)

# platform to enter the text
text_box= Text(root,font="arial 20",bg= "white",relief= GROOVE,wrap=WORD,bd=0)
text_box.place(x=20,y=100,width=680,height=180)

#Gender option
gender_box= Combobox(root,values=["Male","Female"],font= "arial 15 ",state='r',width=15)
gender_box.place(x=100,y=330)
gender_box.set("Male")

#speed option
speed_box= Combobox(root,values=["Fast","Medium","Slow"],font= "arial 15 ",state='r',width=15)
speed_box.place(x=450,y=330)
speed_box.set("Medium")

#Giving Label to both the combobox
Label(root,text="Select Voice",font="arial 15 bold",bg="BLACK",fg="#FF83FA").place(x=100,y=300)

Label(root,text="Select Speed",font="arial 15 bold",bg="BLACK",fg="#FF83FA").place(x=450,y=300)

#play the speech
play_button=Button(root,text="Play", bd='5',bg="white",font=("arial 17 bold"),
                   borderwidth="0.1c",command=speaknow)
play_button.place(x=320,y=400)

root.mainloop()





















#def speech_to_text():
    #convd=converted_speech()
    #input=entry_window
    
        # the input provided by the user is
        # stored in here :test_speech
        #text_speech = pyttsx3.init()
        #text_speech.say(ans)
        #text_speech.runAndWait()
        
       # convd = gTTS(text=text_speech, slow=False, lang=change)
        #convd.save("Speech.mp3")
        #out_window.config(text=text_speech)
