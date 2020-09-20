from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfile
from PyPDF2 import PdfFileReader
def openthefile():
    file = askopenfilename(defaultextention='.pdf', filetypes=[("Pdf files",".Pdf")])
    if "" == file:
        file = None
    else:
        fileEntry.delete(0,END)
        fileEntry.config(fg="blue")
        fileEntry.insert(0,file)
def conversion():
    try:
        pdf = fileEntry.get()
        pdfFile= open(pdf,'rb')
        pdfReader = PdfFileReader(pdfFile)
        pageObject = pdfReader.getPage(0)
        extractedtext = pageObject.extractText()
        readpdf.delete(1.0,END)
        readpdf.insert(INSERT,extractedtext)
        pdfFile.close()
    except FileNotFoundError:
        print("File was not found")
        fileEntry.delete(0,END)
        fileEntry.config(fg="red")
        fileEntry.insert(0,"please select a pdf file first")
    except:
        pass
def savetoword():
    text = str(readpdf.get(1.0,END))
    wordfile = asksaveasfile(mode='w', defaultextension= ".docx",filetypes=[("word file",".doc"),("textfile","txt"),("pythonfile", "py")])
    if wordfile is NONE:
        return
    wordfile.write(text)
    wordfile.close()
    print("has been saved")
    fileEntry.delete(0,END)
    fileEntry.insert(0,"Pdf extracted and saved")
# Front end codes
root = Tk()
root.geometry("800x900")
root.config(bg="black")
root.title("PDF converter machine")
root.resizable(0,0)
try:
    root.wm_iconbitmap("pdf2ico")
except:
    print("icon file is currently not available")
    pass
file = " "
defaultText = "\n\n\n\n\t\t Your extracted text will appear here. \n\t\t you will be able to modify the text too"
appName = Label(root, text="PDF to word converter", font = ("arial",20,"bold"),bg="light blue")
appName.place(x=200,y=5)
labelFile = Label(root,text="select pdf file",font=("arial",10,"bold"))
labelFile.place(x=30,y=50)
fileEntry = Entry(root,font=("calibri", 15),width = 70)
fileEntry.pack(ipadx=200,pady=50,padx=150)
openfilebutton = Button(root, text ="open", font=("arial",12,"bold"),width=30,bg= "blue",fg="yellow",command = openthefile)
openfilebutton.place(x=150,y=85)
converttotext = Button(root, text ="read", font=("arial",12,"bold"),width=30,bg= "blue",fg="yellow",command = conversion)
converttotext.place(x=250,y=150)
readthepdf = Text(root,font=("calibri",12),fg ="red",bg="white",width=65,height=30,bd=15)
readthepdf.pack(padx=20,ipadx=20,pady=20,ipady=20)
readthepdf.insert(INSERT,defaultText)
saveToWord = Button(root, text ="save to word file", font=("arial",12,"bold"),width=30,bg= "yellow",fg="green",command = savetoword)
saveToWord.place(x=230,y=310)
if __name__=='__main__':
    root.mainloop()


