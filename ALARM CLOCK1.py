import datetime
import time
invalid= True
while(invalid):
    print("set a valid time input")
    userInput=input(">>")
    alarmTime=[int(n) for n in userInput.split(":")]
    if alarmTime[0]>=24 or alarmTime[0]<0:
        invalid= True
    elif alarmTime[1]>=60 or alarmTime[1]<0:
        invalid= True
    else:
        invalid =False
    

