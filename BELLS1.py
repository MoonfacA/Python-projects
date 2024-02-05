#Required libraries
from tkinter import  *
import datetime#For current dynamic date and time
import time#orientation of how computer keeps track of time set/for timinmg things(countdown)
import winsound#Provides access to sound-playing machinery


#create an infinite loop
def alarm(set_alarm_timer):
    while True:
        time.sleep(1) #wait for one second
        #For current time
        current_time = datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%y")
        print("The Set Date is:",date)
        print(now)
        if now==set_alarm_timer:
            print("ALARM!")
#Playing the sound
            frequency=1289
            duration=20000
            winsound.Beep(1000, 20000)
            
def actual_time():
    set_alarm_timer=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
            
#Adding labels, frama and button and option menus
clock=Tk()
clock.title("Bells Alarm")
clock.geometry("400x300")
time_format=Label(clock, text="Enter time in 24 hour format!", fg="red",bg="black",font="Ariel").place(x=75,y=120)
addTime=Label(clock,text="Hour :   Min  : Sec",fg="red",font=("Ariel",12,"bold")).place(x=110, y=30)
addTime=Label(clock,text="BELL'S ALARM",fg="orange",font=("Helevetica",19,"bold")).place(x=90, y=0)
setYourAlarm=Label(clock,text="When To Wake You Up?",fg="white",bg="black",relief="solid",font=("Ariel",7,"bold")).place(x=0, y=50)
#Displaying current time on window
#alarm(initialization):
hour=StringVar()
min=StringVar()
sec=StringVar()
print()
hourTime=Entry(clock,textvariable=hour,bg="green",width=15).place(x=110,y=50)

minTime=Entry(clock, textvariable=min,bg="green",width=10).place(x=150,y=50)

secTime=Entry(clock,textvariable=sec,bg="green",width=8).place(x=200,y=50)
#Gathering input
submit=Button(clock,text="Set Alarm",fg="black",width=15,command=actual_time).place(x=120,y=70)

clock.mainloop()
