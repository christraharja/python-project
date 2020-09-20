import tkinter as tk # importing tkinter property
from pytube import YouTube # importing pytube property
root = tk.Tk()
def downloadvideos(): # declaring downloadvideos function
    global e1
    string = e1.get()
    yt = YouTube(str(string))
    videos = yt.get_videos()
    x = 1
    for i in videos:
        print(str(x)+"."+str(v))
        x = x + 1
        n = int(input("Enter your choice"))
        vid = videos[n-1]
        destination = str(input("Enter yourdestination"))
        vid.download(destination)
        print(yt.filename + "\n has been downloaded")
root.title("Youtube Downloader")
a = tk.Label(root,text="Youtube Videos Downloader")
a.pack()
e1 = tk.Entry(root,bd=12)
e1.pack(side = tk.TOP)
Downloadbutton = tk.Button(root,text="Download Videos", fg = "green", command = "downloadvideos")
Downloadbutton.pack(side = tk.BOTTOM)
root.mainloop()



