from tkinter import *
from datetime import date

r = Tk()

d = Entry(r)
m = Entry(r)
y = Entry(r)

d.pack()
m.pack()
y.pack()

l = Label(r)
l.pack()

def age():
    t = date.today()
    a = t.year - int(y.get())
    if (t.month, t.day) < (int(m.get()), int(d.get())):
        a -= 1
    l.config(text="Age: " + str(a))

Button(r, text="Find Age", command=age).pack()

r.mainloop()