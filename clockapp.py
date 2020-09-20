from tkinter import* # importing from tkinter
import datetime # importing datetime property
from tkinter.messagebox import*
from tkinter.ttk import*
import winsound
import sys
import time
from datetime import datetime
alarm = Tk() # initializing alarm first
alarm.title("clock made by Chris")
alarm.geometry("600x500") # determining the size
def alarmclocksystem(): # function for alarm
    if setting.get() == "AM":
        x = int(inputforhours.get())
        y = int(inputforminutes.get())
        z = int(inputforseconds.get())
    if setting.get() == "PM":
        x = int(inputforhours.get()) + 12
        y = int(inputforminutes.get())
        z = int(inputforseconds.get())
    showinfo("The alarm has been set")
    while True:
        if x == datetime.datetime.now().hour and y == datetime.datetime.now().hour and z == datetime.datetime.now().second:
            for i in range(0,100):
                winsound.Beep(10000,100)
            break
def mainclocksystem(): # function for digital time
    currentTime = time.strftime("%H:%M:%S")
    clock.config(text=currentTime)
    clock.after(200,mainclocksystem)
stopOrGo = True
def stop():
    global stopOrGo
    stopOrGo = False
def reset():
    timeStarted.config(text="00:00:00")
def start():
    global stopOrGo
    check= True
    oldtime = time.time()
    minutes = 0
    hours = 0
    minutechange = ""
    secondchange = ""
    lessSixty = 0
    lessSixtyMinutes = 0
    while check:
        alarm.update()
        seconds = time.time() - oldtime

        if seconds - lessSixty < 10:
            secondchange = "0"
        else:
            secondchange = ""

        if minutes < 10:
            minutechange = ""
        else:
            minutechange = ""

        if minutes - lessSixtyMinutes == 60:
            lessSixtyMinutes += 60
            hours += 1

        if seconds - lessSixty > 60:
            lessSixty += 60
            minutes += 1

        timeStarted.config(
            text=str(hours) + ":" + minutechange + str(minutes - lessSixtyMinutes) + ":" + secondchange + str(
                round(seconds - lessSixty, 1)))
t=0 # initialize variable time
def setthetimer():
    global t
    t = t + int(e1.get())
    return t
def countdownsystem():
    global t
    if t > 0:
        print(t)
        lx.config(text=t)
        t-=1
        lx.after(1000,countdownsystem)
    elif t == 0:
        print("end")
        lx.config(text="time is up!")
x1 = Label(alarm,text="Hours:")
x2 = Label(alarm,text="Minutes:")
x3 = Label(alarm,text="Seconds:")
inputforhours = Entry(alarm)
inputforminutes = Entry(alarm)
inputforseconds = Entry(alarm)
setting = Combobox(alarm, values=["AM","PM"])
set = Label(alarm,text="AM OR PM")
setbutton = Button(alarm,text="set alarm",command=alarmclocksystem)
clock = Label(alarm, font = ("times",80,"bold"))
lx = Label(alarm, font = "times 30")
times = StringVar()
e1 = Entry(alarm, textvariable="times")
buttonone = Button(alarm,text="set",width=30,command=setthetimer)
buttontwo = Button(alarm,text="start",width=30,command=countdownsystem)
inputforhours.grid(row=0,column=1)
inputforminutes.grid(row=1,column=1)
inputforseconds.grid(row=2,column=1)
x1.grid(row=0,column=0)
x2.grid(row=1,column=0)
x3.grid(row=2,column=0)
setting.grid(row=0,column=2)
set.grid(row=0,column=4)
setbutton.grid(row=3,column=0)
clock.grid(row=4,column=0)
mainclocksystem()
timeStarted = Label(alarm, text="00:00:00")
timeStarted.grid(row=5,column=0)
startButton = Button(alarm, text="Start", command=start)
startButton.grid(row=6,column=0)
stopButton = Button(alarm, text="Stop", command=stop)
stopButton.grid(row=7,column=0)
resetButton = Button(alarm, text="Reset", command=reset)
resetButton.grid(row=8,column=0)
lx.grid(row=9,column=0)
e1.grid(row=10,column=0)
buttontwo.grid(row=11,column=0)
buttonone.grid(row=11,column=1)
alarm.mainloop()


