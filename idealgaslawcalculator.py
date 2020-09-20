from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
mol = Tk()
mol.configure(bg="green")
mol.geometry("600x900")
mol.title("Idea Gas Law Calculator Built by Chris")
labelformula = Label(mol,text="n = PV/RT")
labelP = Label(mol,text="Please enter the pressure in atm")
labelV = Label(mol,text="Please enter the volume in L")
labelR = Label(mol,text="R is a constant known to be 0.08206")
labelT = Label(mol,text="Please enter the temperature in K")
labeln = Label(mol,text="The mole was found to be in mol")
entryP = Entry(mol)
entryV = Entry(mol)
entryR = Entry(mol)
entryT = Entry(mol)
entryanswer = Entry(mol)
optionT = Combobox(mol,values=["K","C","F"])
optionP = Combobox(mol,values=["atm","torr"])
optionV = Combobox(mol,values=["L","mL"])
global mole
# define function to perform mole calculation
def molcalculation():
	p = float(entryP.get())
	v = float(entryV.get())
	t = float(entryT.get())
	r = 0.08206 # r is constant
	if optionT.get() == "K" and optionP.get() == "atm" and optionV.get() == "L":
		mole = (p * v)/(r * t)
		entryanswer.insert(0,mole)
	if optionT.get() == "K" and optionP.get() == "atm" and optionV.get() == "mL":
		mole = (p * (v/1000))/(r * t)
		entryanswer.insert(0,mole)
	if optionT.get() == "K" and optionP.get() == "torr" and optionV.get() == "L":
		mole = ((p * 0.00131579) * v)/(r * t)
		entryanswer.insert(0,mole)
	if optionT.get() == "K" and optionP.get() == "torr" and optionV.get() == "mL":
		mole = ((p * 0.00131579) * (v/1000))/(r*t)
		entryanswer.insert(0,mole)
	if optionT.get() == "C" and optionP.get() == "atm" and optionV.get() == "L":
		mole = (p * v)/(r * (t + 273.15))
		entryanswer.insert(0,mole)
	if optionT.get() == "C" and optionP.get() == "atm" and optionV.get() == "mL":
		mole = (p * (v/1000))/(r * (t + 273.15))
		entryanswer.insert(0,mole)
	if optionT.get() == "C" and optionP.get() == "torr" and optionV.get() == "L":
		mole = ((p * 0.00131579) * v)/(r * (t + 273.15))
		entryanswer.insert(0,mole)
	if optionT.get() == "C" and optionP.get() == "torr" and optionV.get() == "mL":
		mole = ((p * 0.00131579) * (v/1000))/(r * (t+273.15))
		entryanswer.insert(0,mole)
	if optionT.get() == "F" and optionP.get() == "atm" and optionV.get() == "L":
		mole = (p * v)/(r * (((t - 32) * (5/9)) + 273.15))
		entryanswer.insert(0,mole)
	if optionT.get() == "F" and optionP.get() == "atm" and optionV.get() == "mL":
		mole = (p * (v/1000))/(r * (((t - 32) * (5/9)) + 273.15))
		entryanswer.insert(0,mole)
	if optionT.get() == "F" and optionP.get() == "torr" and optionV.get() == "L":
		mole = ((p * 0.00131579) * v)/(r * (((t - 32) * (5/9)) + 273.15))
		entryanswer.insert(0,mole)
	if optionT.get() == "F" and optionP.get() == "torr" and optionV.get() == "mL":
		mole = ((p * 0.00131579) * (v/1000))/(r * (((t - 32) * (5/9)) + 273.15))
		entryanswer.insert(0,mole)
constantR = 0.08206
entryR.insert(0,constantR)
buttoncalculatemole = Button(mol,text="calculate mol",command=molcalculation)
labelformula.grid(row=0,column=0)
labelP.grid(row=1,column=0)
entryP.grid(row=1,column=1)
optionP.grid(row=1,column=2)
labelV.grid(row=2,column=0)
entryV.grid(row=2,column=1)
optionV.grid(row=2,column=2)
labelR.grid(row=3,column=0)
entryR.grid(row=3,column=1)
labelT.grid(row=4,column=0)
entryT.grid(row=4,column=1)
optionT.grid(row=4,column=2)
labeln.grid(row=5,column=0)
entryanswer.grid(row=5,column=1)
buttoncalculatemole.grid(row=6,column=0)
if __name__ == "__main__":
    mol.mainloop()









