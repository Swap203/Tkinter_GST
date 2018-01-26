from tkinter import *
import os
import backend

def AddProduct():
	backend.insert_product(productCode_value.get(),productName_value.get(),productMRP_value.get(),productBaseRate_value.get(),CGST_value.get(),SGST_value.get())
	window.destroy()
	os.system('python MainWindow.py')

def reset():
	print("Hello")


window=Tk()

window.wm_title("GST MANAGEMENT")

l1=Label(window,text="Product Code")
l1.grid(row=1,column=1)
productCode_value=StringVar()
e1=Entry(window,textvariable=productCode_value)
e1.grid(row=1,column=2)

l2=Label(window,text="Product Name")
l2.grid(row=2,column=1)
productName_value=StringVar()
e2=Entry(window,textvariable=productName_value)
e2.grid(row=2,column=2)


l3=Label(window,text="Price/MRP")
l3.grid(row=3,column=1)
productMRP_value=StringVar()
e3=Entry(window,textvariable=productMRP_value)
e3.grid(row=3,column=2)


l2=Label(window,text="Basic Rate")
l2.grid(row=4,column=1)
productBaseRate_value=StringVar()
e2=Entry(window,textvariable=productBaseRate_value)
e2.grid(row=4,column=2)


l2=Label(window,text="CGST")
l2.grid(row=5,column=1)
CGST_value=StringVar()
e2=Entry(window,textvariable=CGST_value)
e2.grid(row=5,column=2)


l2=Label(window,text="SGST")
l2.grid(row=6,column=1)
SGST_value=StringVar()
e2=Entry(window,textvariable=SGST_value)
e2.grid(row=6,column=2)

b1=Button(window,text="Add Product",width=12,command=AddProduct)
b1.grid(row=7,column=1)

b2=Button(window,text="Reset",width=12, command=reset)
b2.grid(row=7,column=2)


window.mainloop()
