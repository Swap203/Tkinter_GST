from tkinter import *
import os

import backend

def ViewData():
	#print(window.destroy())
	os.system('python ViewData.py')

def AddProduct():
	#window.destroy()
	os.system('python AddProduct.py')


def reset():
	print("Hello")


window=Tk()

window.wm_title("GST MANAGEMENT")

l1=Label(window,text="Select Any Option Below")
l1.grid(row=0,column=1)

b1=Button(window,text="View Data",width=12,command=ViewData)
b1.grid(row=2,column=1)

b2=Button(window,text="Add Product",width=12,command=AddProduct)
b2.grid(row=3,column=1)

b3=Button(window,text="Close",width=12, command=reset)
b3.grid(row=4,column=1)


window.mainloop()
