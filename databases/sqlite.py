"""interacting with sqlite database"""

import sqlite3

#function to create table
def create_table():
    #Step1: Connecting to Database
    conn=sqlite3.connect("lite.db")  #if this file exists, then the connection is made with it, else new db created
    #Step2: Create cursor object to access the rows in database
    cur=conn.cursor()
    #Step3: SQL Query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, qty INTEGER, price FLOAT)")
    #Step4: Commit changes to the database
    conn.commit()
    #Step5: Close the connection
    conn.close()

#function to insert data into table
def insert(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,? )",(item, qty, price))
    conn.commit()
    conn.close()

#function to view the table
def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


