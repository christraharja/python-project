from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
me = Tk()
me.configure(bg="black")
me.geometry("500x600")
me.title("mechanic energy calculator")
labelp = Label(me,text="potential energy")
labelk = Label(me,text="kinetic energy")
labelm = Label(me,text="mechanic energy")
labelmass = Label(me,text="mass")
labelgravity = Label(me,text="gravity constant")
labelheight = Label(me,text="height")
labelvelocity = Label(me,text="velocity")
entryp = Entry(me)
entryk = Entry(me)
entrym = Entry(me)
entrymass = Entry(me)
entryheight = Entry(me)
entryvelocity = Entry(me)
gravityconstant = 10
entrygravity = Entry(me)
entrygravity.insert(0,gravityconstant)
def calculationforp():
	try:
		mass = entrymass.get()
		g = 10
		height = entryheight.get()
		mass = float(mass)
		g = float(g)
		height = float(height)
	except ValueError:
		pass
	res = mass * g * height
	entryp.insert(0,res)
def calculationfork():
	try:
		mass = entrymass.get()
		velocity = entryvelocity.get()
		mass = float(mass)
		velocity = float(velocity)
	except ValueError:
		pass
	res = 0.5 * mass * (velocity)**2
	entryk.insert(0,res)
def calculationform():
	try:
		potential = entryp.get()
		kinetic = entryk.get()
		potential = float(potential)
		kinetic = float(kinetic)
	except ValueError:
		pass
	res = potential + kinetic
	entrym.insert(0,res)
calculatep = Button(me,text="calculate potential energy",command=calculationforp)
calculatek = Button(me,text="calculate kinetic energy", command=calculationfork)
calculatem = Button(me,text="calculate mechanic energy", command=calculationform)
labelmass.grid(row=0,column=0)
entrymass.grid(row=0,column=1)
labelgravity.grid(row=0,column=2)
entrygravity.grid(row=0,column=3)
labelheight.grid(row=0,column=4)
entryheight.grid(row=0,column=5)
labelvelocity.grid(row=0,column=6)
entryvelocity.grid(row=0,column=7)
labelp.grid(row=1,column=0)
entryp.grid(row=1,column=1)
calculatep.grid(row=1,column=2)
labelk.grid(row=2,column=0)
entryk.grid(row=2,column=1)
calculatek.grid(row=2,column=2)
labelm.grid(row=3,column=0)
entrym.grid(row=3,column=1)
calculatem.grid(row=3,column=2)
if __name__ == "__main__":
    me.mainloop()