from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
dc = Tk()
dc.configure(bg="blue")
dc.geometry("800x700")
dc.title("dropshipping profit calculator")
labelpurchasingprice = Label(dc,text="original purchasing price")
labelprofit = Label(dc,text="profit in percentage")
labelsellingprice = Label(dc,text="selling price")
labelquantity = Label(dc,text="total selling quantity")
labeltotalprofit = Label(dc,text="total profit")
labeltax = Label(dc,text="tax")
labelmarketplacefee = Label(dc,text="marketplace fee")
labeltotalprofitafterdeduction = Label(dc,text="total profit after deduction")
entrypurchasingprice = Entry(dc)
entryprofit = Entry(dc)
entrysellingprice = Entry(dc)
entryquatity = Entry(dc)
entrytotalprofit = Entry(dc)
entrytax = Entry(dc)
entrymarketplacefee = Entry(dc)
entrytotalprofitafterdeduction = Entry(dc)
def calculation1():
	try:
		purchasingprice = entrypurchasingprice.get()
		purchasingprice = float(purchasingprice)
		profit = entryprofit.get()
		profit = float(profit)
	except ValueError:
		pass
	sellingprice = (purchasingprice * (profit/100)) + purchasingprice 
	entrysellingprice.insert(0,sellingprice)
def calculation2():
	try:
		purchasingprice = entrypurchasingprice.get()
		purchasingprice = float(purchasingprice)
		profit = entryprofit.get()
		profit = float(profit)
		quantity = entryquatity.get()
		quantity = float(quantity)
	except ValueError:
		pass
	totalprofit = purchasingprice * (profit/100) * quantity
	entrytotalprofit.insert(0,totalprofit)
def calculation3():
	try:
		tax = entrytax.get()
		tax = float(tax)
		fee = entrymarketplacefee.get()
		fee = float(fee)
		totalprofit = entrytotalprofit.get()
		totalprofit = float(totalprofit)
	except ValueError:
		pass
		totalprofitafterdeduction = totalprofit - (tax + fee)
		entrytotalprofitafterdeduction.insert(0,totalprofitafterdeduction)
calculatesp = Button(dc,text="calculate selling price",command=calculation1)
calculatetp = Button(dc,text="calculate total profit",command=calculation2)
calculatetpd = Button(dc,text="calculate total profit after deduction",command=calculation3)
labelpurchasingprice.grid(row=0,column=0)
labelprofit.grid(row=0,column=2)
labelsellingprice.grid(row=0,column=4)
entrypurchasingprice.grid(row=0,column=1)
entryprofit.grid(row=0,column=3)
entrysellingprice.grid(row=0,column=5)
calculatesp.grid(row=0,column=6)
labelquantity.grid(row=1,column=0)
labeltotalprofit.grid(row=1,column=2)
entryquatity.grid(row=1,column=1)
entrytotalprofit.grid(row=1,column=3)
calculatetp.grid(row=1,column=4)
labeltax.grid(row=2,column=0)
labelmarketplacefee.grid(row=2,column=2)
labeltotalprofitafterdeduction.grid(row=2,column=4)
entrytax.grid(row=2,column=1)
entrymarketplacefee.grid(row=2,column=3)
entrytotalprofitafterdeduction.grid(row=2,column=5)
calculatetpd.grid(row=2,column=6)
# creating mainloop
if __name__ == "__main__":
    dc.mainloop()