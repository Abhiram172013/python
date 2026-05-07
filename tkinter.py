from tkinter import *

def mul():
    r.config(text=int(e1.get()) * int(e2.get()))

w = Tk()

e1 = Entry(w)
e2 = Entry(w)
e1.pack()
e2.pack()

Button(w, text="Multiply", command=mul).pack()

r = Label(w, text="")
r.pack()

w.mainloop()