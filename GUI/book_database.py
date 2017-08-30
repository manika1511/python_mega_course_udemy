"""
Program to store following book information:
Title,Author
Year,ISBN

User can:
View records
Search an entry
Add entry
Update Entry
Delete 
Close   

Also there will be text boxes to enter and a scroll bar
"""

from tkinter import *

window = Tk()
l1=Label(window, text="Title")
l1.grid(row=0, column=0)
l2=Label(window, text="Author")
l2.grid(row=0, column=2)
l3=Label(window, text="Year")
l3.grid(row=1, column=0)
l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

b1=Button(window, text="View All")
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry")
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry")
b3.grid(row=4, column=3)

b4=Button(window, text="Update")
b4.grid(row=5, column=3)

b5=Button(window, text="Delete")
b5.grid(row=6, column=3)

b6=Button(window, text="Close")
b6.grid(row=7, column=3)



window.mainloop()








