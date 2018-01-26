from tkinter import *
import os
from openpyxl import Workbook


import backend

def LogIn():
	if backend.check_ValidUser(userName_value.get(),Password_value.get()):
		print("Valid User")
		os.system('python file.py')
	else:
		print("Invalid User")

def toEXCEL():
	wb = Workbook()
	ws = wb.create_sheet(0)
	ws.title = "My Data"
	ws.append(["SN", "Product Code", "Product Name", "Product MRP","Product Basic Rate","Quantity", "CGST", "CGST Rate", "SGST", "SGST Rate", "Total"])
	for row in data:
		ws.append(row)
	workbook_name = "test_workbook"
	wb.save(workbook_name + ".xlsx")

window=Tk()

window.wm_title("GST MANAGEMENT")

l1=Label(window,text="SN")
l1.grid(row=0,column=0)

l2=Label(window,text="Product Code")
l2.grid(row=0,column=1)

l3=Label(window,text="Product Name")
l3.grid(row=0,column=2)

l4=Label(window,text="MRP")
l4.grid(row=0,column=3)

l5=Label(window,text="Basic Rate")
l5.grid(row=0,column=4)

l10=Label(window,text="QTY")
l10.grid(row=0,column=5)

l6=Label(window,text="CGST (%)")
l6.grid(row=0,column=6)

l7=Label(window,text="CGST Rate")
l7.grid(row=0,column=7)

l8=Label(window,text="SGST (%)")
l8.grid(row=0,column=8)

l9=Label(window,text="SGST Rate")
l9.grid(row=0,column=9)



l11=Label(window,text="Total")
l11.grid(row=0,column=10)

data=backend.view_all_product_data_purchases()

for index, dat in enumerate(data):
	Label(window, text=dat[0]).grid(row=index+1, column=0)
	Label(window, text=dat[1]).grid(row=index+1, column=1)
	Label(window, text=dat[2]).grid(row=index+1, column=2)
	Label(window, text=dat[3]).grid(row=index+1, column=3)
	Label(window, text=dat[4]).grid(row=index+1, column=4)
	Label(window, text=dat[5]).grid(row=index+1, column=5)
	Label(window, text=dat[6]).grid(row=index+1, column=6)
	Label(window, text=dat[7]).grid(row=index+1, column=7)
	Label(window, text=dat[8]).grid(row=index+1, column=8)
	Label(window, text=dat[9]).grid(row=index+1, column=9)
	Label(window, text=dat[10]).grid(row=index+1, column=10)
	last_index=index

b1=Button(window,text="To EXCEL",width=12, command=toEXCEL)
b1.grid(row=last_index+3,column=5)


window.mainloop()
