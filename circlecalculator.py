from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
import math
crc = Tk()
crc.configure(bg="dark blue")
crc.geometry("800x1000")
crc.title("circle calculator made by Chris")
labeltype = Label(crc,text="what are you trying to calculate? please select options next here")
circletype = Label(crc,text="please select what type of circle")
option1 = Combobox(crc,values=["area","circumferences"])
option2 = Combobox(crc,values=["full circle","half circle","three fourth circle","quarter circle"])
labelr = Label(crc,text="please enter the radius of the circle")
entryr = Entry(crc)
labelanswer = Label(crc,text="the calculated answer is")
entryanswer = Entry(crc)
global area
global circumference
# Formula for area of a circle is pi*r^2
# Formula for circumference of a circle is 2*pi*r
def calculatecircle():
	radius = float(entryr.get())
	if option1.get() == "area" and option2.get() == "full circle":
		area = math.pi * (radius**2)
		entryanswer.insert(0,area)
	if option1.get() == "area" and option2.get() == "half circle":
		area = math.pi * (radius**2) * (1/2)
		entryanswer.insert(0,area)
	if option1.get() == "area" and option2.get() == "three fourth circle":
		area = math.pi * (radius**2) * (3/4)
		entryanswer.insert(0,area)
	if option1.get() == "area" and option2.get() == "quarter circle":
		area = math.pi * (radius**2) * (1/4)
		entryanswer.insert(0,area)
	if option1.get() == "circumferences" and option2.get() == "full circle":
		circumference = math.pi * radius * 2
		entryanswer.insert(0,circumference)
	if option1.get() == "circumferences" and option2.get() == "half circle":
		circumference = math.pi * radius * 2 * (1/2)
		entryanswer.insert(0,circumference)
	if option1.get() == "circumferences" and option2.get() == "three fourth circle":
		circumference = math.pi * radius * 2 * (3/4)
		entryanswer.insert(0,circumference)
	if option1.get() == "circumferences" and option2.get() == "quarter circle":
		circumference == math.pi *radius * 2 * (1/4)
		entryanswer.insert(0,circumference)
buttoncalculation = Button(crc,text="calculate",command=calculatecircle)
labeltype.grid(row=0,column=0)
option1.grid(row=0,column=1)
circletype.grid(row=1,column=0)
option2.grid(row=1,column=1)
labelr.grid(row=2,column=0)
entryr.grid(row=2,column=1)
buttoncalculation.grid(row=3,column=0)
labelanswer.grid(row=4,column=0)
entryanswer.grid(row=4,column=1)
if __name__ == "__main__":
    crc.mainloop()

