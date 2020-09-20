from tkinter import* # importing tkinter property
import pyttsx3 # importing pyttsx3 property

root = Tk()
root.title("text to speech app")
root.geometry("600x900")

def talking():
    machine = pyttsx3.init()
    # machine.setProperty('rate',995)
    voices = machine.getProperty("voices")
    machine.setProperty('voice',voices[1].id)
    machine.say(myentry.get())
    machine.runAndWait()
    myentry.delete(0,END)

myentry = Entry(root,font=("Helvetica",30))
myentry.pack(pady=25)
mybutton = Button(root, text="speak",command = talking)
mybutton.pack(pady=30)
root.mainloop()



