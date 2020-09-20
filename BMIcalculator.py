from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import*
bmi = Tk()
bmi.configure(bg="dark orange")
bmi.geometry("500x600")
bmi.title("bmi calculator made by Chris")
labelweight = Label(bmi,text="Enter your weight in kg")
labelheight = Label(bmi,text="Enter your height in cm")
labelresult = Label(bmi,text="Your BMI value is:")
labelcategory = Label(bmi,text="Your BMI index lies on this category")
optweight = Combobox(bmi,values=["kg","lbs"])
optheight = Combobox(bmi,values=["cm","inches"])
entryweight = Entry(bmi)
entryheight = Entry(bmi)
entryres = Entry(bmi)
bmicategory = Entry(bmi)
global bmivalue
global BMIcat
def calculate():
	weight = float(entryweight.get())
	height = float(entryheight.get())
	if optweight.get() == "kg" and optheight.get() == "cm":
		bmivalue = weight/((height/100)**2)
		entryres.insert(0,bmivalue)
	if optweight.get() == "kg" and optheight.get() == "inches":
		bmivalue = weight/((height * 0.0254)**2)
		entryres.insert(0,bmivalue)
	if optweight.get() == "lbs" and optheight.get() == "cm":
		bmivalue = (weight * 0.453592)/((height/100)**2)
		entrtres.insert(0,bmivalue)
	if optweight.get() == "lbs" and optheight.get() == "inches":
		bmivalue = (weight * 0.453592)/((height * 0.0254)**2)
		entryres.insert(0,bmivalue)
def definecategory():
	weight = float(entryweight.get())
	height = float(entryheight.get())
	bmivalue = weight/((height/100)**2)
	if bmivalue <= 18.5:
		BMIcat = "underweight"
		bmicategory.insert(0,BMIcat)
	if bmivalue > 18.5 and bmivalue <= 25:
		BMIcat = "normal"
		bmicategory.insert(0,BMIcat)
	if bmivalue > 25 and bmivalue <= 30:
		BMIcat = "overweight"
		bmicategory.insert(0,BMIcat)
	if bmivalue > 30 and bmivalue <= 35:
		BMIcat = "obese"
		bmicategory.insert(0,BMIcat)
	if bmivalue > 35:
		BMIcat = "extremly obese"
		bmicategory.insert(0,BMIcat)
calculateButton = Button(bmi,text="calculate bmi",command=calculate)
defineButton = Button(bmi,text="define category",command=definecategory)
labelweight.grid(row=0,column=0)
labelheight.grid(row=1,column=0)
entryweight.grid(row=0,column=1)
entryheight.grid(row=1,column=1)
optweight.grid(row=0,column=2)
optheight.grid(row=1,column=2)
calculateButton.grid(row=2,column=0)
entryres.grid(row=2,column=1)
labelcategory.grid(row=3,column=0)
bmicategory.grid(row=3,column=1)
defineButton.grid(row=4,column=0)
if __name__ == "__main__":
    bmi.mainloop()