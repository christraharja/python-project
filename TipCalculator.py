from tkinter import *
from tkinter.ttk import*
from tkinter.messagebox import *
tip = Tk()
tip.configure(bg="purple")
tip.geometry("700x500")
tip.title("Tip calculator made by Chris")
labelOne = Label(tip,text="Please enter the payment amount")
inputOne = Entry(tip)
labelTwo = Label(tip,text="Please select the percentage of the tip")
option = Combobox(tip, values = ["5%","10%","15%","20%","25%","30%"])
labelThree = Label(tip,text="The tip is calculated to be")
labelFour = Label(tip,text="The total payment including tip is =")
tipamount = Entry(tip)
totalamount = Entry(tip)
global tipamt
def tipcalculation():
	if option.get() == "5%":
		tipamt = float(inputOne.get()) * 0.05
		tipamount.insert(0,tipamt)
	if option.get() == "10%":
		tipamt = float(inputOne.get()) * 0.10
		tipamount.insert(0,tipamt)
	if option.get() == "15%":
		tipamt = float(inputOne.get()) * 0.15
		tipamount.insert(0,tipamt)
	if option.get() == "20%":
		tipamt = float(inputOne.get()) * 0.20
		tipamount.insert(0,tipamt)
	if option.get() == "25%":
		tipamt = float(inputOne.get()) * 0.25
		tipamount.insert(0,tipamt)
	if option.get() == "30%":
		tipamt = float(inputOne.get()) * 0.30
		tipamount.insert(0,tipamt)
def totalcalculation():
	if option.get() == "5%":
		tipamt = float(inputOne.get()) * 0.05
		totalamount.insert(0,tipamt + float(inputOne.get()))
	if option.get() == "10%":
		tipamt = float(inputOne.get()) * 0.10
		totalamount.insert(0, tipamt + float(inputOne.get()))
	if option.get() == "15%":
		tipamt = float(inputOne.get()) * 0.15
		totalamount.insert(0, tipamt + float(inputOne.get()))
	if option.get() == "20%":
		tipamt = float(inputOne.get()) * 0.20
		totalamount.insert(0, tipamt + float(inputOne.get()))
	if option.get() == "25%":
		tipamt = float(inputOne.get()) * 0.25
		totalamount.insert(0, tipamt + float(inputOne.get()))
	if option.get() == "30%":
		tipamt = float(inputOne.get()) * 0.30
		totalamount.insert(0, tipamt + float(inputOne.get()))
calculationbutton1 = Button(tip,text="calculate", command=tipcalculation)
calculationbutton2 = Button(tip,text="calculate",command=totalcalculation)
labelOne.grid(row=0,column=0)
inputOne.grid(row=0,column=1)
labelTwo.grid(row=1,column=0)
option.grid(row=1,column=1)
labelThree.grid(row=2,column=0)
tipamount.grid(row=2,column=1)
calculationbutton1.grid(row=3,column=0)
calculationbutton2.grid(row=5,column=0)
labelFour.grid(row=4,column=0)
totalamount.grid(row=4,column=1)
if __name__ == "__main__":
    tip.mainloop()

