from tkinter import *

window=Tk()

def km_to_miles():
    miles=float(input_val.get())*1.6
    t1.insert(END, miles)

b1=Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0, column=3)

input_val=StringVar()

l1=Label(window, text="Kilometers")
l1.grid(row=0, column=0)

e1=Entry(window, textvariable=input_val)
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=10)
t1.grid(row=0, column=2)

window.mainloop()