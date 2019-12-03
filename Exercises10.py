from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.colorchooser import *
from tkinter import scrolledtext
from tkinter.colorchooser import *
# =============================================================================
#                                   Exercise 1
# =============================================================================

root = Tk()

name = Label(root, text = "Name").grid(row = 0, column=0)
n = StringVar()
entry_one = Entry(root, textvariable = n).grid(row = 0, column = 1)
password = Label(root, text="Password").grid(row=1, column=0)
p = StringVar()
entry_two = Entry(root, textvariable = p).grid(row = 1, column=1)

def checkUser():
    if n.get() == "Orange" and p.get() == "CodingAcademy" :
        print("Successful login")
    else:
        print("Wrong User Name or Password")
submit = Button(root, text="Submit", command = checkUser).grid(row=4, column=0)

root.mainloop()

# =============================================================================
#                                   Exercise 2
# =============================================================================

win = Tk()

def messageShow():
    messagebox.showinfo("figure 1","this is a message")
    
def showForm():
    c = Toplevel(win)
    c.geometry("300x200")
    number = Label(c, text="Emp Number").place(x=10, y=10)
    name = Label(c, text="Emp Name").place(x=10, y=30)
    btn = Button(c,text="Exit",command=c.destroy).place(x=10, y=60)
    
    e1 = Entry(c).place(x = 90, y= 10)
    e2 = Entry(c).place(x = 90, y= 30)


def scrollView():
    v = Toplevel(win)
    v.title("Child Window 2")
    v.geometry('300x200')
    txt = scrolledtext.ScrolledText(v, width=40, height=10)
    txt.grid(column=0, row=0)
    for n in range(20):
        print("The count is ", n)

    
b1 = Button(win, text="Open message", command=messageShow)
b2 = Button(win, text="Open child window 1", command=showForm)
b3 = Button(win, text="Open child window 2", command = scrollView)
b1.pack()
b2.pack()
b3.pack()



win.mainloop()


# =============================================================================
#                                   Exercise 3
# =============================================================================
col = Tk()
col.geometry("400x250")
def getColor():
    color = askcolor()
    col.configure(background = color[1])
Button(text="Select Color", command = getColor).pack()
mainloop()






























