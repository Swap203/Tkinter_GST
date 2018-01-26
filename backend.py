import sqlite3

def db_connect():
	conn=sqlite3.connect("GSTMgmt.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS userDetails (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS productDetails (id INTEGER PRIMARY KEY, productCode TEXT, productName TEXT,productMRP FLOAT, productBaseRate FLOAT,CGST FLOAT, SGST FLOAT)")
	cur.execute("CREATE TABLE IF NOT EXISTS purchaseDetails(id INTEGER PRIMARY KEY,	QTY INTEGER, SoldDate INTEGER, productId INTEGER, FOREIGN KEY(productId) REFERENCES productDetails(id))")
	#cur.execute("DELETE FROM productDetails WHERE id=4")
	#cur.execute("DELETE FROM purchaseDetails WHERE id=4")
	conn.commit()
	conn.close()

def insert_user(username,password):
	conn=sqlite3.connect("GSTMgmt.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO userDetails VALUES(NULL,?,?)",(username,password))
	conn.commit()
	conn.close()

def insert_product(productCode,productName,productMRP,productBaseRate,CGST,SGST):
	conn=sqlite3.connect("GSTMgmt.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO productDetails VALUES(NULL,?,?,?,?,?,?)",(productCode,productName,productMRP,productBaseRate,CGST,SGST))
	conn.commit()
	conn.close()

def view_all_product_data_purchases():
    conn=sqlite3.connect("GSTMgmt.db")
    cur=conn.cursor()
    cur.execute("SELECT *,ROUND((CGSTRATE+SGSTRATE+productBaseRate*QTY),2) AS 'Total' FROM (SELECT productDetails.id,productCode,productName,productMRP,productBaseRate,QTY,CGST, (productBaseRate*QTY*CGST/100) AS 'CGSTRATE' ,SGST, (productBaseRate*QTY*SGST/100) AS 'SGSTRATE' FROM productDetails LEFT OUTER JOIN purchaseDetails ON productDetails.ID = purchaseDetails.productId)")
    rows=cur.fetchall()
    conn.close()
    return rows





def insert_purchase(QTY,SoldDate,productId):
	conn=sqlite3.connect("GSTMgmt.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO purchaseDetails VALUES(NULL,?,?,?)",(QTY,SoldDate,productId))
	conn.commit()
	conn.close()






def view_all_product_data():
    conn=sqlite3.connect("GSTMgmt.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM productDetails")
    rows=cur.fetchall()
    conn.close()
    return rows



def check_ValidUser(username,password):
	conn=sqlite3.connect("GSTMgmt.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM userDetails WHERE username=? AND password=?",(username,password))
	rows=cur.fetchall()
	conn.close()
	if rows:
		return True
	else:
		return False


db_connect()
#insert_user("Swapnil","password")
#insert_product(2000,"GoodDayCashw",10,7.70,9.00,9.00)
#insert_product(2001,"GoodDayCashw",20,15.40,9.00,9.00)
#insert_purchase(12,10,1)
#insert_purchase(10,10,2)
