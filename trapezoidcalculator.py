from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
tc = Tk()
tc.configure(bg="brown")
tc.geometry("800x750")
tc.title("trapezoid area calculator")
labeltopside = Label(tc, text="input the top side")
labelbottomside = Label(tc, text="input the bottom side")
labelleftside = Label(tc, text="input the left side")
labelrightside = Label(tc, text="input the right side")
labelheight = Label(tc, text="input the height")
labelarea = Label(tc, text="the area of trapezoid")
labelperimeter = Label(tc, text="the perimeter of trapezoid")
entrytopside = Entry(tc)
entrybottomside = Entry(tc)
entryheight = Entry(tc)
entryarea = Entry(tc)
entryleftside = Entry(tc)
entryrightside = Entry(tc)
entryperimeter = Entry(tc)
# Function to calculate area of the trapezoid
def calculationarea():
	try:
		top = entrytopside.get()
		bottom = entrybottomside.get()
		height = entryheight.get()
		top = float(top)
		bottom = float(bottom)
		height = float(height)
	except ValueError:
		pass
	a = ((top+bottom) * height)/2
	entryarea.insert(0,a)
# Function to calculate perimeter of the trapezoid
def calculationperimeter():
	try:
		top = entrytopside.get()
		bottom = entrybottomside.get()
		right = entryrightside.get()
		left = entryleftside.get()
		top = float(top)
		bottom = float(bottom)
		right = float(right)
		left = float(left)
	except ValueError:
		pass
	pt = top + bottom + left + right
	entryperimeter.insert(0,pt)
# Frontend
calculationarea = Button(tc, text="calculate area", command=calculationarea)
calculationperimeter = Button(tc, text="calculationperimeter", command=calculationperimeter)
labeltopside.grid(row=0,column=0)
labelbottomside.grid(row=0,column=1)
labelheight.grid(row=0,column=2)
entrytopside.grid(row=1,column=0)
entrybottomside.grid(row=1,column=1)
entryheight.grid(row=1,column=2)
labelleftside.grid(row=2,column=0)
labelrightside.grid(row=2,column=1)
entryleftside.grid(row=3,column=0)
entryrightside.grid(row=3,column=1)
labelarea.grid(row=4,column=0)
entryarea.grid(row=4,column=1)
calculationarea.grid(row=4,column=2)
labelperimeter.grid(row=5,column=0)
entryperimeter.grid(row=5,column=1)
calculationperimeter.grid(row=5,column=2)
if __name__ == "__main__":
    tc.mainloop()
