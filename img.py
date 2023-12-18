import tkinter
from tkinter import *
from tkinter import messagebox
from monitor import monitor

def btnclick():
    messagebox.showinfo("Message","Button is clicked")

root = tkinter.Tk()
root.geometry("1000x1800")

photo = PhotoImage(file="icons/monitor.png")
photo2 = PhotoImage(file="icons/monitor.png")
btn = Button(
    root,
    image=photo,
    command=monitor,
    border=0,
   
    height=90,
    width=180,
    
)
btn.pack(pady=(20,10))

btn2 = Button(
    root,
    image=photo2,
    command=btnclick,
    border=0,
)
btn2.pack()
root.mainloop()
