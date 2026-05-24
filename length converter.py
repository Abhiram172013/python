from tkinter import *

def convert():
    cm.set(float(i.get()) * 2.54)

r = Tk()

i = StringVar()
cm = DoubleVar()

Entry(r, textvariable=i).pack()
Button(r, text="Convert", command=convert).pack()
Label(r, textvariable=cm).pack()

r.mainloop()