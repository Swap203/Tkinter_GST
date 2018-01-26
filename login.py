from tkinter import *
import os
import backend

def LogIn():
	if backend.check_ValidUser(userName_value.get(),Password_value.get()):
		print("Valid User")
		window.destroy()
		os.system('python MainWindow.py')
	else:
		print("Invalid User")

def reset():
	print("Hello")


window=Tk()

window.wm_title("GST MANAGEMENT")

l1=Label(window,text="User Name")
l1.grid(row=0,column=0)
userName_value=StringVar()
e1=Entry(window,textvariable=userName_value)
e1.grid(row=0,column=1)

l2=Label(window,text="Password")
l2.grid(row=1,column=0)
Password_value=StringVar()
e2=Entry(window,show="*",textvariable=Password_value)
e2.grid(row=1,column=1)


b1=Button(window,text="Log In",width=12,command=LogIn)
b1.grid(row=2,column=0)

b2=Button(window,text="Reset",width=12, command=reset)
b2.grid(row=2,column=1)


window.mainloop()
