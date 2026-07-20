from tkinter import *
import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="smit2007",
    database="CollegeDB"
)
cur=con.cursor()

def insert():
    r=roll_no.get()
    n=name.get()
    a=age.get()
    g=gender.get()
    ci=city.get()
    co=course.get()
    m=marks.get()

    query="INSERT INTO Student(Roll_No,Name,Age,Gender,City,Course,Marks) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values=(r,n,a,g,ci,co,m)
    cur.execute(query,values)
    con.commit()
    print("Successfully Inserted")

def delete_fn():
    d=delete.get()
    query="DELETE FROM Student WHERE Roll_No=%s"
    cur.execute(query,[d])
    con.commit()
    print("Data Deleted")


root=Tk()
root.title("Insertion & Deletion in DataBase")
root.geometry("500x500")

rollno=Label(root,text="Enter Roll No:")
rollno.grid(row=0,column=0)

roll_no=Entry(root,width=20)
roll_no.grid(row=0,column=1)

lbl_name=Label(root,text="Enter Name:")
lbl_name.grid(row=1,column=0)

name=Entry(root,width=20)
name.grid(row=1,column=1)

lbl_age=Label(root,text="Enter Age:")
lbl_age.grid(row=2,column=0)

age=Entry(root,width=20)
age.grid(row=2,column=1)

lbl_gender=Label(root,text="Enter gender:")
lbl_gender.grid(row=3,column=0)

gender=Entry(root,width=20)
gender.grid(row=3,column=1)

lbl_course=Label(root,text="Enter Course:")
lbl_course.grid(row=4,column=0)

course=Entry(root,width=20)
course.grid(row=4,column=1)

lbl_city=Label(root,text="Enter City:")
lbl_city.grid(row=5,column=0)

city=Entry(root,width=20)
city.grid(row=5,column=1)

lbl_marks=Label(root,text="Enter Marks:")
lbl_marks.grid(row=6,column=0)

marks=Entry(root,width=20)
marks.grid(row=6,column=1)

insert_btn=Button(root,text="Insert",command=insert)
insert_btn.grid(row=7,column=0,columnspan=2)

lbl_delete=Label(root,text="Enter Roll No you want to delete:")
lbl_delete.grid(row=8,column=0)

delete=Entry(root,width=20)
delete.grid(row=8,column=1)

delete_btn=Button(root,text="Delete",command=delete_fn)
delete_btn.grid(row=9,column=0,columnspan=2)

root.mainloop()
cur.close()
con.close()