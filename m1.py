import tkinter as tk
import tkinter.font as font
#from in_out import in_out
from rect_noise import rect_noise
from motion import noise
from tkinter import Tk,Label
from record import record
from PIL import Image, ImageTk
from tkinter import Tk,Label
from time import sleep

class LoadingSplash:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SMART CCTV")
        #self.window.iconphoto(False, tk.PhotoImage(file='mn.png'))
        #self.window.geometry('1380x720+0+0')
        # self.window.resizable(False,False)
        self.window.config(bg="black")
        self.window.attributes("-fullscreen",True)
        Label(self.window,text="Loading...",font="Bahnschrift 15",
              bg="black",fg="#FFBD09").place(x=490,y=320)

        #loading blocks
        for i in range(16):
            Label(self.window,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)

        self.window.update()
        self.animation()
        self.main()
        
        self.window.mainloop()

        

        #loader animation
    def animation(self):
        for i in range(200):
            for j in range(16):
                Label(self.window,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
                sleep(0.06)
                self.window.update_idletasks()
                    #make block dark
                Label(self.window,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
        self.window.destroy()
    window.after(3000,self.main)
    """else:
            self.window.destroy()
            exit()"""
    
    def main():
        self.window = tk.Tk()
        self.window.title("SMART CCTV")
        self.window.config(bg="black")
        self.window.attributes("-fullscreen",True)

        self.window.mainloop()
    
if __name__=="__main__":
    LoadingSplash()
"""
frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart CCTV Camera")
label_font = font.Font(size=35, weight='bold',family='Times New Roman')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/spy.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)   
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green', image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='orange', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10))

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)


btn6 = tk.Button(frame1, text='In Out', height=90, width=180, fg='green', image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=4, pady=(20,10), column=2)

btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2)

frame1.pack()
window.mainloop()
"""


