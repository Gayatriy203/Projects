import time
from tkinter import *
from tkinter import messagebox
import winsound
from winsound import PlaySound

 
# creating Tk window
root = Tk()

  
# setting geometry of tk window
root.geometry("300x300")
  
# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")
root.config(bg='cyan')
  
# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

#Titles
Title_hour= Button(root, text="Hour", bg="white", fg="black",
                     font=("Times New Roman", 10, "bold"))
Title_hour.place(x=80, y=50)

Title_minute= Button(root, text="Minute", bg="white", fg="black",
                     font=("Times New Roman", 9, "bold"))
Title_minute.place(x=130, y=50)

Title_second= Button(root, text="Second", bg="white", fg="black",
                     font=("Times New Roman", 9, "bold"))
Title_second.place(x=190, y=50)
  
# Use of Entry class to take input from the user
hourEntry= Entry(root, width=2, font=("Times New Roman",20,""),
                 textvariable=hour)
hourEntry.place(x=82,y=20)
  
minuteEntry= Entry(root, width=2, font=("Times New Roman",20,""),
                   textvariable=minute)
minuteEntry.place(x=135,y=20)
  
secondEntry= Entry(root, width=2, font=("Times New Roman",20,""),
                   textvariable=second)
secondEntry.place(x=195,y=20)


  
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
  
        # when temp value = 0; then play sound 
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
            winsound.PlaySound('bell.wav',winsound.SND_FILENAME)
             
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
# button widget
btn = Button(root, text='   Start   ', bd='5',bg="white",fg="black",
             font=("Times New Roman", 13, "bold"),command= submit)
btn.place(x = 120,y = 110)

# creating pause button
#pause_button = Button(root, text=" Pause ",bd='5', bg="white", fg="black",
                    # font=("Times New Roman", 13, "bold"), command=submit)
#pause_button.place(x=120, y=160)
#creating reset button
#reset_button = Button(root, text=" Reset ",bd='5', bg="white", fg="black",
                     #font=("Times New Roman", 13, "bold"), command=submit)
#reset_button.place(x=120, y=210)
           
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()