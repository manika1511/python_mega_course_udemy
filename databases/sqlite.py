"""interacting with sqlite database"""

import sqlite3

#Step1: Connecting to Database
conn=sqlite3.connect("lite.db")  #if this file exists, then the connection is made with it, else new db created

#Step2: Create cursor object to access the rows in database
cur=conn.cursor()

#Step3: SQL Query
cur.execute("CREATE TABLE store (item TEXT, qty INTEGER, price FLOAT)")

#Step4: Commit changes to the database
conn.commit()

#Step5: Close the connection
conn.close()
