import psycopg2

#function to create table
def create_table():
    #Step1: Connecting to Database
    conn=psycopg2.connect("dbname='<database_name>' user='<user_name>' password=<> host=<> port=<>")
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
    conn = psycopg2.connect("dbname='<database_name>' user='<user_name>' password=<> host=<> port=<>")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,price,item)) #use this format to prevent SQL Injection
    conn.commit()
    conn.close()

#function to view the table
def view():
    conn = psycopg2.connect("dbname='<database_name>' user='<user_name>' password=<> host=<> port=<>")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

#function to delete an entry in the table
def delete(item):
    conn = psycopg2.connect("dbname='<database_name>' user='<user_name>' password=<> host=<> port=<>")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

#function to update an entry in the table
def update(qty,price,item):
    conn = psycopg2.connect("dbname='<database_name>' user='<user_name>' password=<> host=<> port=<>")
    cur = conn.cursor()
    cur.execute("UPDATE store SET qty=%s, price=%s WHERE item=%s", (qty,price,item))
    conn.commit()
    conn.close()


