from tkinter import *
from tkinter import messagebox, ttk
import pymysql


#----------window----------
root = Tk(className="Register")	  
root.attributes('-fullscreen',True)
root.configure(bg="White")


#----------register Label----------
label_register = Label(root, text="REGISTER", bg="white", fg="#FF5252", font="georgia 30 bold").place(x=650,y=80)


#----------firstname entry----------
label_firstname = Label(root, text="First Name", bg="white", fg="black", font="georgia 15 bold").place(x=180,y=200)
firstname = StringVar()
entry_firstname = Entry(root, textvariable=firstname, font="verdana 13", bg="lightgrey").place(x=180,y=230,width=350,height=35)


#----------lastname entry----------
label_lastname = Label(root, text="Last Name", bg="white", fg="black", font="georgia 15 bold").place(x=990,y=200)
lastname = StringVar()
entry_lastname = Entry(root, textvariable=lastname, font="verdana 13", bg="lightgrey").place(x=990,y=230,width=350,height=35)


#----------contact number entry----------
label_contact = Label(root, text="Contact Number", bg="white", fg="black", font="georgia 15 bold").place(x=180,y=300)
contact = StringVar()
entry_contact = Entry(root, textvariable=contact, font="verdana 13", bg="lightgrey").place(x=180,y=330,width=350,height=35)


#----------email entry----------
label_email = Label(root, text="Email", bg="white", fg="black", font="georgia 15 bold").place(x=990,y=300)
email = StringVar()
entry_email = Entry(root, textvariable=email, font="verdana 13", bg="lightgrey").place(x=990,y=330,width=350,height=35)


#----------security question entry----------
label_question = Label(root, text="Security Question", bg="white", fg="black", font="georgia 15 bold").place(x=180,y=400)
question = StringVar()
combo_question = ttk.Combobox(root, textvariable=question, font="verdana 13", state="readonly", justify=CENTER)
combo_question["values"] = ("Select","Your First Girlfriend Name","Your First Crush Name","Your Best Friend Name","Your First School Name")
combo_question.place(x=180,y=430,width=350,height=35)
combo_question.current(0)


#----------answer entry----------
label_answer = Label(root, text="Answer", bg="white", fg="black", font="georgia 15 bold").place(x=990,y=400)
answer = StringVar()
entry_answer = Entry(root, textvariable=answer, font="verdana 13", bg="lightgrey").place(x=990,y=430,width=350,height=35)


#----------password entry----------
label_password = Label(root, text="Password", bg="white", fg="black", font="georgia 15 bold").place(x=180,y=500)
password = StringVar()
entry_password = Entry(root, textvariable=password, show="*", font="verdana 13", bg="lightgrey").place(x=180,y=530,width=350,height=35)


#----------confirm password entry----------
label_confirmpass = Label(root, text="Confirm Password", bg="white", fg="black", font="georgia 15 bold").place(x=990,y=500)
confirmpass = StringVar()
entry_confirmpass = Entry(root, textvariable=confirmpass, show="*", font="verdana 13", bg="lightgrey").place(x=990,y=530,width=350,height=35)


def redirect_login():
	root.destroy()
	import main


def clear():
	firstname.set('')
	lastname.set('')
	contact.set('')
	email.set('')
	answer.set('')
	password.set('')
	confirmpass.set('')
	combo_question.current(0)


def register_data():
	if firstname.get()=="" or lastname.get()=="" or contact.get()=="" or email.get()=="" or question.get()=="Select" or answer.get()=="" or password.get()=="" or confirmpass.get()=="":
		messagebox.showerror("Error","All fields are required.", parent=root)
	elif password.get()!=confirmpass.get():
		messagebox.showerror("Error","Password & Confirm Password should be same.", parent=root)
	elif check.get()==0:
		messagebox.showerror("Error","Please Agree our terms & conditions.", parent=root)
	else:
		try:
			mydb = pymysql.connect(user='root',host='localhost',passwd='root')
			mycursor = mydb.cursor()
			mycursor.execute("create database if not exists AI_Surveillance_System")
			mycursor.execute("use AI_Surveillance_System")
			mycursor.execute("create table if not exists user (id int(10) auto_increment, primary key(id), f_name varchar(50), l_name varchar(50), contact varchar(10), email varchar(50), question varchar(100), answer varchar(100), password varchar(50))")
			mycursor.execute("select * from user where email = %s", email.get())
			row = mycursor.fetchone()
			if row!=None:
				messagebox.showerror("Error","User already exists, please try with another email.", parent=root)
			else:
				mycursor.execute("insert into user (f_name, l_name, contact, email, question, answer, password) values(%s, %s, %s, %s, %s, %s, %s)",
									(
										firstname.get(), lastname.get(), contact.get(), email.get(), question.get(), answer.get(), password.get() 
									))
				mydb.commit()
				mydb.close()
				messagebox.showinfo("Success","Registration successful.", parent=root)
				clear()
		except Exception as es:
			messagebox.showerror("Error",f"Error due to : {str(es)}", parent=root)	


#----------T&C checkbox----------
check = IntVar()
button_check = Checkbutton(root, text="I Agree The Terms & Conditions", variable=check, onvalue=1, offvalue=0, bg="white", fg="black", font="georgia 13 bold").place(x=180,y=580)


#----------register button----------
button_register = Button(root, command=register_data, text="Register",cursor="hand2", width=20, height=1, bg="#FF5252", bd=0, fg="white", font="georgia 15 bold").place(x=690,y=680,width=180,height=40)


#----------login button----------
# button_login = Button(root, command=redirect_login, text="Log In",cursor="hand2", width=20,bg="white", bd=0, fg="black", font="georgia 15").place(x=1300,y=720)

button_login = Button(root, command=redirect_login, text="Log In", cursor="hand2", width=20, height=1, bg="#FF5252", bd=0, fg="white", font="georgia 15 bold").place(x=1300, y=720, width=100, height=40)
root.mainloop()
