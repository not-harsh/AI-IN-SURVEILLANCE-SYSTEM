from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pymysql


class Login_window:
	def __init__(self, root):
		#----------window----------
		self.root = root
		self.root.title("Login")	  
		self.root.attributes('-fullscreen',True)
		self.root.configure(bg="black")
		
		#----------icon----------
		self.image = ImageTk.PhotoImage(file="icons/spy2.png")
		image = Label(self.root, image=self.image, bd=0, bg="black").place(x=625,y=40,height=250,width=300)
		
		#----------email entry----------
		email = Label(self.root, text="Email", bg="black", fg="white", font="georgia 15 bold").place(x=742,y=295)
		self.email_entry = Entry(self.root, font="verdana 13", bg="lightgrey")
		self.email_entry.place(x=600,y=325,width=350,height=35)
		
		#----------password entry----------
		password = Label(self.root, text="Password", bg="black", fg="white", font="georgia 15 bold").place(x=725,y=385)
		self.pass_entry = Entry(self.root, show='*', font="verdana 13", bg="lightgrey")  
		self.pass_entry.place(x=600,y=415,width=350,height=35)
		
		#----------register button----------
		button_register = Button(self.root, command=self.redirect_register, text="Register New Account?", cursor="hand2", bg="black", fg="red", bd=0, font="georgia 12").place(x=600,y=460)
		
		#----------login button----------
		button_login = Button(self.root, command=self.login, text="Login", cursor="hand2", width=20, height=1, bg="red", bd=0, fg="white", font="georgia 15 bold").place(x=690,y=525,width=180,height=40)

		#----------forgot password button----------
		button_forget = Button(self.root, command=self.forget_password_window, text="Forget Password?", cursor="hand2", bg="black", fg="red", bd=0, font="georgia 12").place(x=825,y=575)


	def clear(self):
		self.combo_question.current(0)
		self.answer_entry.delete(0, END)
		self.newpass_entry.delete(0, END)
		self.email_entry.delete(0, END)
		self.pass_entry.delete(0, END)


	def forget_password(self):
		if self.combo_question.get()=="Select" or self.answer_entry.get()=="" or self.newpass_entry.get()=="":
			messagebox.showerror("Error","All fields are required.", parent=self.new_root)
		else:
			try:
				mydb = pymysql.connect(user='root', host='localhost', passwd='', database='AI_Surveillance_System')
				mycursor = mydb.cursor()
				mycursor.execute("select * from user where email=%s and question=%s and answer=%s", (self.email_entry.get(), self.combo_question.get(), self.answer_entry.get()))
				new_row = mycursor.fetchone()
				if new_row==None:
					messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer.", parent=self.new_root)
				else:
					mycursor.execute("update user set password=%s where email=%s", (self.newpass_entry.get(), self.email_entry.get()))
					mydb.commit()
					mydb.close()
					messagebox.showinfo("Success","Your Password has been reset, Login again.", parent=self.new_root)
					self.clear()
					self.new_root.destroy()
			except Exception as es:
				messagebox.showerror("Error",f"Error due to : {str(es)}", parent=new_root)


	def forget_password_window(self):
		if self.email_entry.get()=="":
			messagebox.showerror("Error","Please enter the email address to reset your password.", parent=self.root)
		else:
			try:
				mydb = pymysql.connect(user='root', host='localhost', passwd='', database='AI_Surveillance_System')
				mycursor = mydb.cursor()
				mycursor.execute("select * from user where email=%s", self.email_entry.get())
				row = mycursor.fetchone()
				if row==None:
					messagebox.showerror("Error","Please enter the valid email address to reset your password.", parent=root)
				else:
					mydb.close()
					#----------window----------
					self.new_root = Tk()
					self.new_root.title("Forget Password")
					self.new_root.attributes('-fullscreen',True)
					self.new_root.configure(bg="black")
					self.new_root.focus_force()
					self.new_root.grab_set()

					#----------reset password label----------
					label_forgetpass = Label(self.new_root, text="Reset   Password", bg="black", fg="red", font="georgia 30 bold").place(x=600,y=50)
								
					#----------security question entry----------
					label_question = Label(self.new_root, text="Security Question", bg="black", fg="white", font="georgia 15 bold").place(x=600,y=200)
					self.combo_question = ttk.Combobox(self.new_root, font="verdana 13", state="readonly", justify=CENTER)
					self.combo_question['values'] = ("Select","Your First Girlfriend Name","Your First Crush Name","Your Best Friend Name","Your First School Name")
					self.combo_question.place(x=600,y=230,width=350,height=35)
					self.combo_question.current(0)
					
					#----------answer entry----------
					label_answer = Label(self.new_root, text="Answer", bg="black", fg="white", font="georgia 15 bold").place(x=600,y=350)
					self.answer_entry = Entry(self.new_root, font="verdana 13", bg="lightgrey")
					self.answer_entry.place(x=600,y=380,width=350,height=35)

					#----------new password entry----------
					label_newpass = Label(self.new_root, text="New Password", bg="black", fg="white", font="georgia 15 bold").place(x=600,y=500)
					self.newpass_entry = Entry(self.new_root, show="*", font="verdana 13", bg="lightgrey")
					self.newpass_entry.place(x=600,y=530,width=350,height=35)
					
					#----------reset password button----------
					button_resetpass = Button(self.new_root, command=self.forget_password, text="Reset", cursor="hand2", width=20, height=1, bg="red", bd=0, fg="white", font="georgia 15 bold").place(x=690,y=650,width=180,height=40)
					
			except Exception as es:
				messagebox.showerror("Error",f"Error due to : {str(es)}", parent=self.root)


	def redirect_register(self):
		self.root.destroy()
		import register 


	def login(self):
		if self.email_entry.get()=="" or self.pass_entry.get()=="":
			messagebox.showerror("Error","All fields are required.", parent=self.root)
		else:
			try:
				mydb = pymysql.connect(user='root', host='localhost', passwd='', database='AI_Surveillance_System')
				mycursor = mydb.cursor()
				mycursor.execute("select * from user where email=%s and password=%s", (self.email_entry.get(),self.pass_entry.get()))
				row = mycursor.fetchone()
				if row==None:
					messagebox.showerror("Error","Invalid email or password.", parent=self.root)
				else:
					self.root.destroy()
					import screen
				mydb.close()
			except Exception as es:
				messagebox.showerror("Error",f"Error due to : {str(es)}", parent=self.root)

root = Tk()
obj = Login_window(root)
root.mainloop()
