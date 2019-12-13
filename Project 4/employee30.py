from flask import Flask, redirect, url_for, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ======================== get from DATABASE ======================#

@app.route('/login', methods = ["POST"])
def login():
    msg = ""
    if request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]
            with sqlite3.connect("Org.db") as con:
                cur = con.cursor()
                cur.execute("SELECT UserName, Password FROM Login where UserName='%s' and Password = '%s'"%(username,password))
                rows = cur.fetchall()
                
                if rows:
                    msg="Done"
                    return render_template('Home.html')

                else:
                    return render_template('index.html')
        except:
            con.rollback()
            msg = "faild login"





@app.route('/logout')
def logout():
    return redirect("/")


@app.route('/department')
def department():
      return render_template('add_department.html')
  
#====================== insert to DATABASE ========================#
  
    
@app.route('/addepartment',methods=["GET","POST"])
def addDepartment():
   msg = "msg"
   if request.method == "POST":
        try:
            departmentName = request.form["deptname"]
            locationName = request.form["locID"]
            with sqlite3.connect("Org.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into departments (department_name, location_id) values (?,?)", (departmentName, locationName))

                con.commit()
                msg = "Successfully Add Department"
        except:
            con.rollback()
            msg = "we can not the Department to the list"
        finally:
            return render_template('add_department.html', msg=msg)
        
#====================== Get all departments ========================#            
            
@app.route('/showdepartment')
def showdepartment():
        con = sqlite3.connect("Org.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from departments")
        rows = cur.fetchall()
        return render_template('show_dapartment.html',rows = rows)


#====================== Get all employees ========================#   

@app.route("/viewemployees",methods=["POST","GET"])
def view_employees():
    if request.method == "POST":
        depid=request.form["info"]
        with sqlite3.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("select * from employees where department_id = ?", depid)
            rows = cur.fetchall()
        return render_template("showEmployees.html",rows=rows)

    
#====================== Delete employee ========================#   
        
@app.route("/delete",methods=["POST","GET"])
def delete():
    delete_id=request.form["rip"]
    with sqlite3.connect("Org.db") as con:
        cur = con.cursor()
        cur.execute("delete from employees where employee_id = ?",delete_id)
        con.commit()
        msg="Employee Deleted Successfully!"
    return render_template("Home.html",msg=msg)


#====================== Update employee ========================#  

@app.route("/update",methods=["POST","GET"])
def update():
    if request.method == "POST":
        id=request.form["id"]
        with sqlite3.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("select * from employees where employee_id = ?", id)
            rows = cur.fetchall()
        return render_template("UpdateEmployee.html",rows=rows)


@app.route("/updateform",methods=["POST","GET"])
def updateform():
    if request.method == "POST":
        fname=request.form["fname"]
        lname=request.form["lname"]
        email=request.form["email"]
        phone=request.form["phone"]
        hdate=request.form["hdate"]
        job=request.form["job"]
        salary=request.form["salary"]
        empid = request.form["id"]
        with sqlite3.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("update employees set first_name = ?,last_name=?,email=?,phone_number=?,hire_date=?,job_id=?,salary=? where employee_id = ?",(fname, lname, email, phone, hdate, job, salary, empid))
            con.commit()
            msg="Employee Updated Successfully!"
        return render_template("Home.html",msg=msg)
  
        


if __name__ == '__main__':
    app.run()