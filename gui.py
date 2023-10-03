from tkinter import *

def onEnter():
    print(e1.get())
    print(e2.get())
    print(e3.get())
    print(e4.get())

root = Tk()

root.title("Portfolio Balancer")

t1 = Label(root, text="Check Amount:").pack()
e1 = Entry(root)
e1.pack()
t2 = Label(root, text="Savings Amount:").pack()
e2 = Entry(root)
e2.pack()
t3 = Label(root, text="Bonds Amount:").pack()
e3 = Entry(root)
e3.pack()
t4 = Label(root, text="Stocks Amount:").pack()
e4 = Entry(root)
e4.pack()
ebttn = Button(root, text="Enter", command=onEnter).pack()

root.mainloop()
