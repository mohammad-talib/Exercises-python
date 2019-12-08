import tkinter.scrolledtext as ScrolledText
from tkinter import *

import sqlite3

conn = sqlite3.connect("OrgDB.db")
#c = conn.cursor()
#
#
#c.execute('''CREATE TABLE Employees(EmployeeNumber int, EmployeeName text, EmployeeGender text, EmployeeNationality text, EmployeeDateofBirth text, EmployeeAddress text, EmployeeDepartment text, EmployeeSalary real)''')
#
#


root = Tk()
root.title('Employee App')
root.geometry('300x250+810+415')

#======================= insert data ===========================#

def employee():
    def subAddEmp():
        
        c = conn.cursor()
        c.execute("INSERT INTO Employees (EmployeeNumber, EmployeeName, EmployeeGender, EmployeeNationality, EmployeeDateofBirth, EmployeeAddress, EmployeeDepartment, EmployeeSalary) VALUES (?,?,?,?,?,?,?,?)", ((int(num.get()),names.get(),gender.get(), nationality.get(), dateofBirth.get(), address.get(), department.get(), float(salary.get()))))
        conn.commit()
#        conn.close()
        print("OK")
        
        
    c = Toplevel(root)
    c.geometry("300x300+810+415")
    number = Label(c, text="Employee Number").place(x=10, y=10)
    name = Label(c, text="Employee Name").place(x=10, y=40)
    Gender = Label(c, text="Gender").place(x=10, y=70)
    Nationality = Label(c, text="Nationality").place(x=10, y=100)
    DateofBirth = Label(c, text="Date of Birth").place(x=10, y=130)
    Address = Label(c, text="Address").place(x=10, y=160)
    Department = Label(c, text="Department").place(x=10, y=190)
    Salary = Label(c, text="Salary").place(x=10, y=220)
    add = Button(c,text="Add",command=subAddEmp).place(x=10, y=250)

    num = StringVar()
    employee_number= Entry(c, textvariable = num).place(x = 120, y= 10)
    names = StringVar()
    name = Entry(c, textvariable = names).place(x = 120, y= 40)
    gender = StringVar()
    Gender= Entry(c, textvariable = gender).place(x = 120, y= 70)
    nationality = StringVar()
    Nationality = Entry(c, textvariable = nationality).place(x = 120, y= 100)
    dateofBirth = StringVar()
    DateofBirth= Entry(c, textvariable = dateofBirth).place(x = 120, y= 130)
    address = StringVar()
    Address = Entry(c, textvariable = address).place(x = 120, y= 160)
    department = StringVar()
    Department = Entry(c, textvariable = department).place(x = 120, y= 190)
    salary = StringVar()
    Salary = Entry(c, textvariable = salary).place(x = 120, y= 220)
    exitform = Button(c,text="Exit",command=c.destroy).place(x=120, y=250)

#======================= show data =====================#

def viewEmployee():
        viewchild = Toplevel(root)
        st = ScrolledText.ScrolledText(viewchild)
        st.pack()
        c = conn.cursor()
        
        for s in enumerate(c.execute("SELECT * FROM Employees")):
                st.insert(INSERT,s)
                st.insert(INSERT, "\n")

    
#======================================================================#

addEmployee = Button(root,text="Add Employee",command=employee).place(x=100, y=60)  
viewEmployee = Button(root,text="View Employee",command=viewEmployee).place(x=100, y=120)





root.mainloop()