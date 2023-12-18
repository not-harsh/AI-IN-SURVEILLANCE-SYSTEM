import socket
import tkinter as tk
from tkinter import font, Label, Button
from PIL import Image, ImageTk
from in_out import in_out
from motion import noise
from monitor import monitor
from rect_noise import rect_noise
from record import record
from detection import detection
from night_vision import night_vision

def create_button(frame, text, command, image_path):
    btn_image = Image.open(image_path)
    btn_image = btn_image.resize((180, 90), Image.ANTIALIAS)
    btn_image = ImageTk.PhotoImage(btn_image)

    btn_font = font.Font(size=25)
    button = Button(frame, text=text, height=90, width=180, command=command,
                    image=btn_image, compound='left', bg='black', borderwidth=0, fg='green', font=btn_font)
    button.image = btn_image  # To prevent image garbage collection
    return button

def create_label(frame, image_path):
    icon = Image.open(image_path)
    icon = icon.resize((150, 150), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(icon)

    label_icon = Label(frame, image=icon, bg='black')
    label_icon.image = icon  # To prevent image garbage collection
    return label_icon

def create_title_label(frame, text, font_size=35):
    label_title = Label(frame, text=text, bg='black', fg='white')
    label_font = font.Font(size=font_size, weight='bold', family='Times New Roman')
    label_title['font'] = label_font
    return label_title

def screen(window):
    frame1 = tk.Frame(window, bg="black")
    frame1.grid(row=0, column=0, padx=10, pady=10)

    label_title = create_title_label(frame1, "AI Surveillance System")
    label_title.grid(row=0, column=2, pady=(10, 10))

    label_icon = create_label(frame1, 'icons/spy.png')
    label_icon.grid(row=1, pady=(5, 10), column=2)

    btn1 = create_button(frame1, "Monitor", monitor, 'icons/monitor.png')
    btn1.grid(row=2, pady=(20, 10))

    btn2 = create_button(frame1, "Rectangle Noise", rect_noise, 'icons/rectangle.png')
    btn2.grid(row=2, column=1, pady=(20, 10), padx=(20, 5))

    btn3 = create_button(frame1, "Motion", noise, 'icons/motion.png')
    btn3.grid(row=3, pady=(20, 10))

    btn4 = create_button(frame1, "Record", record, 'icons/record.png')
    btn4.grid(row=3, column=1, pady=(20, 10))

    btn5 = create_button(frame1, "Exit", window.destroy, 'icons/exit.png')
    btn5.grid(row=4, pady=(20, 10), column=2)

    btn6 = create_button(frame1, "In/Out", in_out, 'icons/inout.png')
    btn6.grid(row=2, pady=(20, 10), column=2)

    btn7 = create_button(frame1, "Detection", detection, 'icons/detection.png')
    btn7.grid(row=1, pady=(20, 10), column=2)

    btn8 = create_button(frame1, "Night Vision", night_vision, 'icons/night_vision.png')
    btn8.grid(row=3, pady=(20, 10), column=2)

def blocks(window):
    for i in range(16):
        Label(window, bg="#1F2732", width=2, height=1).place(x=(i + 22) * 22, y=350)
        window.update()
        animation(window)
        window.mainloop()

def animation(window):
    import time
    for i in range(3):
        for j in range(16):
            Label(window, bg="#FFBD09", width=2, height=1).place(x=(j + 22) * 22, y=350)
            window.update_idletasks()
            time.sleep(0.03)
            Label(window, bg="#1F2732", width=2, height=1).place(x=(j + 22) * 22, y=350)
    screen(window)

def fun():
    window = tk.Tk()
    window.title("AI Surveillance System")
    window.config(bg="black")
    window.attributes("-fullscreen", True)
    hostname = socket.gethostname()
    socket.gethostbyname(hostname)

    label_loading = Label(window, text="Loading...", font="Bahnschrift 15", bg="black", fg="#FFBD09")
    label_loading.place(relx=0.5, rely=0.5, anchor='center')

    blocks(window)
    window.overrideredirect(1)

fun()
