import socket as socket
import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from monitor import monitor
from rect_noise import rect_noise
from record import record
from detection import detection
from night_vision import night_vision
from PIL import Image, ImageTk
from tkinter import Tk,Label

def screen(window):
    def new_win():
        """window.destroy()
        window1 = tk.Tk()
        window1.title("AI Surveillance System")
        window1.config(bg="black")
        window1.attributes("-fullscreen",True)"""
        frame1 = tk.Frame(window)
        frame1.config(bg="black")
        label_title = tk.Label(frame1, text="AI Surveillance System", bg='black', fg='white')
        label_font = font.Font(size=35, weight='bold',family='Times New Roman')
        label_title['font'] = label_font
        label_title.grid(pady=(10,10), column=2)
    
    
        icon = Image.open('icons/spy.png')
        icon = icon.resize((150,150), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        label_icon = tk.Label(frame1, image=icon, bg='black')   
        label_icon.grid(row=1, pady=(5,10), column=2)
    
        btn1_image = Image.open('icons/monitor.png')
        btn1_image = btn1_image.resize((180,90), Image.ANTIALIAS)
        btn1_image = ImageTk.PhotoImage(btn1_image)
    
        btn2_image = Image.open('icons/rectangle.png')
        btn2_image = btn2_image.resize((180,90), Image.ANTIALIAS)
        btn2_image = ImageTk.PhotoImage(btn2_image)
    
        btn3_image = Image.open('icons/motion.png')
        btn3_image = btn3_image.resize((180,90), Image.ANTIALIAS)
        btn3_image = ImageTk.PhotoImage(btn3_image)

        btn4_image = Image.open('icons/record.png')
        btn4_image = btn4_image.resize((180,90), Image.ANTIALIAS)
        btn4_image = ImageTk.PhotoImage(btn4_image)
    
        btn5_image = Image.open('icons/exit.png')
        btn5_image = btn5_image.resize((180,90), Image.ANTIALIAS)
        btn5_image = ImageTk.PhotoImage(btn5_image)
    
        btn6_image = Image.open('icons/inout.png')
        btn6_image = btn6_image.resize((180,90), Image.ANTIALIAS)
        btn6_image = ImageTk.PhotoImage(btn6_image)

        btn7_image = Image.open('icons/detection.png')
        btn7_image = btn7_image.resize((180,90), Image.ANTIALIAS)
        btn7_image = ImageTk.PhotoImage(btn7_image)

        btn8_image = Image.open('icons/night_vision.png')
        btn8_image = btn8_image.resize((180,90), Image.ANTIALIAS)
        btn8_image = ImageTk.PhotoImage(btn8_image)
    
        # --------------- Button -------------------#
        btn_font = font.Font(size=25)
        btn1 = tk.Button(frame1, height=90, width=180, fg='green',command=monitor, image=btn1_image, compound='left' ,bg='black',borderwidth = 0 )
        btn1['font'] = btn_font
        btn1.grid(row=3, pady=(20,10))
    
        btn2 = tk.Button(frame1, height=90, width=180, fg='orange',command=rect_noise, image=btn2_image, compound='left' ,bg='black',borderwidth = 0)
        btn2['font'] = btn_font
        btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))
    
        btn_font = font.Font(size=25)
        btn3 = tk.Button(frame1, height=90, width=180, fg='green',command=noise, image=btn3_image, compound='left' ,bg='black',borderwidth = 0 )
        btn3['font'] = btn_font
        btn3.grid(row=5, pady=(20,10))
    
        btn4 = tk.Button(frame1, height=90, width=180,command=record,image=btn4_image, compound='left' ,bg='black',borderwidth = 0 )
        btn4['font'] = btn_font
        btn4.grid(row=5, pady=(20,10), column=3)
    
        btn5 = tk.Button(frame1, height=90, width=180, fg='green',command=window.destroy, image=btn5_image ,bg='black',compound='left',borderwidth = 0 )
        btn5['font'] = btn_font
        btn5.grid(row=6, pady=(20,10), column=2)
    
        btn6 = tk.Button(frame1, height=90, width=180, fg='green',command=in_out, image=btn6_image ,bg='black',compound='left', borderwidth = 0 )
        btn6['font'] = btn_font
        btn6.grid(row=3, pady=(20,10), column=2)

        btn7 = tk.Button(frame1, height=90, width=180, fg='green',command=detection, image=btn7_image ,bg='black',compound='left', borderwidth = 0 )
        btn7['font'] = btn_font
        btn7.grid(row=2, pady=(20,10), column=2)
        
        btn8 = tk.Button(frame1, height=90, width=180, fg='green',command=night_vision, image=btn8_image ,bg='black',compound='left', borderwidth = 0 )
        btn8['font'] = btn_font
        btn8.grid(row=5, pady=(20,10), column=2)

        frame1.pack()
        window.mainloop()
        
    def blocks():
        
        for i in range(16):
            Label(window,bg="#000000",width=2,height=1).place(x=(i+22)*22,y=350)
            
            window.update()
            animation()
        
            window.mainloop()
            
        
       
    def animation(): 
        import time

        for i in range(3):
            for j in range(16):
                Label(window,bg="#FF5252",width=2,height=1).place(x=(j+22)*22,y=350)
                
                window.update_idletasks()
                time.sleep(0.03)
                Label(window,bg="#000000",width=2,height=1).place(x=(j+22)*22,y=350)
        new_win()
            
        window.mainloop()
        
    blocks()
    
def fun():
    window = tk.Tk()
    window.title("AI Surveillance System")
    window.config(bg="black")
    window.attributes("-fullscreen",True)
    hostname = socket.gethostname()
    socket.gethostbyname(hostname)
    #Label(window,text="AI Surveillance System",font="Marlett 15",bg="black",fg="#000000").place(x=490,y=20)
    Label(window,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FF5252").place(x=600,y=320)
    screen(window)
    window.overrideredirect(1)

fun()