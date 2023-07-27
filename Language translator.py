import tkinter as tk
from tkinter import *
from googletrans import Translator
from gtts import gTTS

def translate_language():
    n1 = entry_window.get()
    n2 = Translator()
    n3 = drop_down.get()

    if n3 == "Hindi":
        change = "hi"
    elif n3 == "English":
        change = "en"
    elif n3 == "Spanish":
        change = "es"
    elif n3 == "German":
        change = "de"
    elif n3 == "French":
        change = "fr"
    elif n3 == "Marathi":
        change = "mr"
    elif n3 == "Telugu":
        change = "te"
    elif n3 == "Russian":
        change = "ru"
    elif n3 == "arabic":
        change = "ar"
    elif n3 == "italian":
        change = "it"

    text_translate = n2.translate(n1, dest=change)
    text_translate = text_translate.text
    
    n4 = gTTS(text=text_translate, slow=False, lang=change)
    n4.save("translated.mp3")
    out_window.config(text=text_translate)

lang_options = [
    "Hindi",
    "English",
    "Spanish",
    "German",
    "French",
    "Marathi",
    "Telugu",
    "Russian",
    "arabic",
    "italian"
]

tk_window = tk.Tk()
tk_window.geometry("800x500")
tk_window.config(bg='maroon')

entry_window = Entry(tk_window, bg="white", fg="black",
                     font=("Times New Roman", 25, "bold"))
entry_window.place(x=240, y=40)

drop_down = StringVar()
drop_down.set("Select Language")

list_lang = OptionMenu(tk_window, drop_down, *lang_options)
list_lang.configure(background="white", fg="black", font=("Times New Roman", 16, "bold"))
list_lang.place(x=300, y=140)

translate_b = Button(tk_window, text="Translate!", bg="white", fg="black",
                     font=("Times New Roman", 25, "bold"), command=translate_language)
translate_b.place(x=310, y=220)



out_window = Label(tk_window, text="\n\t\t\t\t\t\t\t\t\t", bg="White", fg="Black",
                  font=("Times New Roman", 16, "bold"))
out_window.place(x=0, y=320)

trans_label = Label(tk_window, text="*^^*Translated Language*^^*",bg="white",fg="black",
                    font=("Times New Roman", 16, "bold"))
trans_label.place(x=240, y=420)



tk_window.mainloop()


