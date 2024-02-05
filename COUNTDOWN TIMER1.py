#Required libraries
from tkinter import  *
import datetime#For current dynamic date and time
import time#orientation of how computer keeps track of time set/for timinmg things(countdown)
import winsound#Provides access to sound-playing machineryfrom threading import Timer#Libraries used
from threading import Timer

#Creating the window
window=Tk()
window.title("Countdown timer")
window.geometry("800x800")
head=Label(window, text="COUNTDOWN TIMER", font=("calibri"))
head.pack(pady=20)#Displaying header without specifying co-ordinates
Label(window,text="Enter time in HH:MM:SS", font=("bold")).pack()

#Defining functions
def countdown():
    t=count.get()
    while t:
        mins, secs=divmod(t,60)
        display=("{:02d}:{:02d}".format(mins,secs))
        time.sleep(1)
        t-=1
        Label(window,text= display).pack.pack()
    Label(window,text="TIME UP", font=("bold",20)).place(x=250,y=290)
    frequency=1289
    duration=20000
    winsound.Beep(1000, 20000)
#Input entry buttons
Entry(window,textvariable="hour",width=30).pack()
Entry(window,textvariable="minute",width=30).pack()
Entry(window,textvariable="second",width=30).pack()

#Set countdown button
Button(window,text="Set Countdown",command=countdown,bg="yellow").place(x=250,y=230)
#Displaying current time on window
now=datetime.datetime.now()
current_time=now.strftime("%H:%M:%S")
Label(window,text=current_time).pack()
        
window.mainloop()