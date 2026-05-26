from tkinter import *

def calc():
    p = float(e1.get())
    t = float(e2.get())
    r = float(e3.get())

    si = (p * t * r) / 100
    ci = p * ((1 + r / 100) ** t) - p

    l4.config(text="Simple Interest = " + str(round(si, 2)))
    l5.config(text="Compound Interest = " + str(round(ci, 2)))

root = Tk()
root.title("Interest Calculator")

Label(root, text="Principal").grid(row=0, column=0)
Label(root, text="Time").grid(row=1, column=0)
Label(root, text="Rate").grid(row=2, column=0)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(root, text="Calculate", command=calc).grid(row=3, column=1)

l4 = Label(root, text="")
l5 = Label(root, text="")

l4.grid(row=4, column=0, columnspan=2)
l5.grid(row=5, column=0, columnspan=2)

root.mainloop()