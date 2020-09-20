from tkinter import * # importing tkinter property
import math # importing math property
from tkinter.messagebox import*
from tkinter.ttk import*
app = Tk()
app.configure(bg="light blue")
app.geometry("800x900")
app.title("height calculator predictor made by Chris")
opt = Combobox(app, values= ["male","female"])
estHeight = Entry(app)
estHeight.grid(row=1,column=3)
global expectedHeight
def estimatedHeight():
    if opt.get() == "male":
        z1 = float(inputFather.get())
        z2 = float(inputMother.get())
        estHeight.insert(0,(z1 +z2 + 13)/2)
    if opt.get() == "female":
        z1 = float(inputFather.get())
        z2 = float(inputMother.get())
        estHeight.insert(0,(z1 +z2 - 13)/2)
z1 = Label(app,text="father's height")
z2 = Label(app,text="mother's height")
z3 = Label(app,text="Estimated height")
zCalculate = Button(app,text="calculate",command=estimatedHeight)
inputFather = Entry(app)
inputMother = Entry(app)
zCalculate.grid(row=1,column=2)
z1.grid(row=0,column=0)
z2.grid(row=1,column=0)
z3.grid(row=0,column=3)
inputFather.grid(row=0,column=1)
inputMother.grid(row=1,column=1)
opt.grid(row=0, column=2)
if __name__ == "__main__":
    app.mainloop()
