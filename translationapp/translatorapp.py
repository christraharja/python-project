from tkinter import *
from tkinter.messagebox import*
from tkinter.ttk import*
from googletrans import Translator
from method import thetranslator
tr = Tk()
tr.title("translation app made by Chris")
tr.geometry("1000x950")
tr.configure(bg="light green")
tr.resizable(0,0)
def get():
    i = inilangs.get()
    d = destlangs.get()
    inputfromuser = sourceText.get(1.0,END)
    translator = thetranslator()
    t = translator.run(txt=inputfromuser,src=i,dest=d)
    desttext.delete(1.0,END)
    desttext.insert(END,t)
appName = Label(tr, text="translation app")
appName.pack(side=TOP,fill=BOTH,pady=0)
frame = Frame(tr).pack(side=BOTTOM)
sourceText = Text(frame,wrap=WORD)
sourceText.pack(side=TOP ,padx=5,pady=5)
translatebutton = Button(frame, text="translate",command=get)
translatebutton.pack(side=TOP,pady=15)
languageoptions = thetranslator().languageoptions
inilangs = Combobox(frame,values=languageoptions,width=10)
inilangs.set("english")
inilangs.place(x=30,y=290)
destlangs = Combobox(frame,values=languageoptions,width=10)
destlangs.set("english")
destlangs.place(x=870,y=290)
desttext = Text(frame,wrap=WORD)
desttext.pack(side=TOP,padx=5,pady=5)
if __name__ == "__main__":
    tr.mainloop()






