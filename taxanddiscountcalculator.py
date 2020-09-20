from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
tax = Tk()
tax.configure(bg="purple")
tax.geometry("800x750")
tax.title("tax and discount calculator made by Chris")
labelprice = Label(tax,text="please enter the original price")
entryprice = Entry(tax)
labeltax = Label(tax,text="please enter the tax in percentage")
entrytax =Entry(tax)
labeldiscount = Label(tax,text="please enter the discount in percentage")
entrydiscount = Entry(tax)
labelafterdiscount = Label(tax,text="after discount")
entryad = Entry(tax)
labeltotalprice = Label(tax,text="the calculated price after tax and discount is")
entrytotalprice = Entry(tax)
global initialprice
global aftertax
global afterdiscount
global totalprice
def calculatediscount():
	discountamt = float(entrydiscount.get())
	initialprice = float(entryprice.get())
	afterdiscount = initialprice - initialprice * (discountamt/100)
	entryad.insert(0,afterdiscount)
def calculatetax():
	discountamt = float(entrydiscount.get())
	initialprice = float(entryprice.get())
	afterdiscount = initialprice - initialprice * (discountamt/100)
	taxamt = float(entrytax.get())
	initialprice = float(entryprice.get())
	aftertax = afterdiscount + afterdiscount * (taxamt/100)
	entrytotalprice.insert(0,aftertax)
buttonaftertax = Button(tax,text="calculate",command=calculatetax)
buttonafterdiscount = Button(tax,text="calculate",command=calculatediscount)
labelprice.grid(row=0,column=0)
entryprice.grid(row=0,column=1)
labeltax.grid(row=3,column=0)
entrytax.grid(row=3,column=1)
labeldiscount.grid(row=1,column=0)
entrydiscount.grid(row=1,column=1)
labelafterdiscount.grid(row=1,column=2)
entryad.grid(row=1,column=3)
buttonafterdiscount.grid(row=2,column=0)
labeltotalprice.grid(row=5,column=0)
entrytotalprice.grid(row=5,column=1)
buttonaftertax.grid(row=5,column=2)
if __name__ == "__main__":
    tax.mainloop()