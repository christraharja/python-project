from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
cmc = Tk()
cmc.configure(bg="dark blue")
cmc.geometry("1000x800")
cmc.title("commission based calculator")
labelproductfees = Label(cmc, text="product's price ")
labelcommission = Label(cmc, text="commission per product in percentage")
labeltotalrewardforsales = Label(cmc, text="total reward")
entryproductfees = Entry(cmc)
entrycommission = Entry(cmc)
entrytotalrewardforsales = Entry(cmc)
labelquantityofsales = Label(cmc, text="number of sales")
entryquantityofsales = Entry(cmc)
labeltotalpaymenttosalesteam = Label(cmc, text="total payment to sales team")
entrytotalpaymenttosalesteam = Entry(cmc)
labeltax = Label(cmc, text="total tax in percentage")
entrytax = Entry(cmc)
labeltotalaftertax = Label(cmc, text="total fees after tax")
entrytotalpaymentincludingtax = Entry(cmc)
# Function to calculate commission per product
def calculation1():
    try:
        pf = entryproductfees.get()
        pf = float(pf)
        commission = entrycommission.get()
        commission = float(commission)
    except ValueError:
        pass
    tr = ((commission/100) * pf) + pf
    entrytotalrewardforsales.insert(0,tr)
# Function to calculate total commission for the sales team
def calculation2():
    try:
        qs = entryquantityofsales.get()
        qs = float(qs)
        t = entrytotalrewardforsales.get()
        t = float(t)
    except ValueError:
        pass
    total = qs * t
    entrytotalpaymenttosalesteam.insert(0,total)
# Function to calculate total payment after tax
def calculation3():
    try:
        tax = entrytax.get()
        tax = float(tax)
        totalp = entrytotalpaymenttosalesteam.get()
        totalp = float(totalp)
    except ValueError:
        pass
    total = ((tax/100) * totalp) + totalp
    entrytotalpaymentincludingtax.insert(0,total)
# Frontend
calculate1 = Button(cmc, text="calculate fees including commission", command=calculation1)
calculate2 = Button(cmc, text="calculate total fees for the sales team", command=calculation2)
calculate3 = Button(cmc, text="calculate total fees after tax", command=calculation3)
labelproductfees.grid(row=0,column=0)
labelcommission.grid(row=0,column=1)
labeltotalrewardforsales.grid(row=0,column=2)
entryproductfees.grid(row=1,column=0)
entrycommission.grid(row=1,column=1)
entrytotalrewardforsales.grid(row=1,column=2)
calculate1.grid(row=2,column=0)
labelquantityofsales.grid(row=3,column=0)
labeltotalpaymenttosalesteam.grid(row=3,column=1)
entryquantityofsales.grid(row=4,column=0)
entrytotalpaymenttosalesteam.grid(row=4,column=1)
calculate2.grid(row=5,column=0)
labeltax.grid(row=6,column=0)
entrytax.grid(row=6,column=1)
labeltotalaftertax.grid(row=7,column=0)
entrytotalpaymentincludingtax.grid(row=7,column=1)
calculate3.grid(row=8,column=0)
# Constructing mainloop
if __name__ == "__main__":
    cmc.mainloop()