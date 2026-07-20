from tkinter import *
import mysql.connector

root = Tk()
root.title("Student Search")
root.geometry("700x400")

def search():
    listbox.delete(0, END)

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="smit2007",
        database="CollegeDB"
    )

    cur = con.cursor()
# query = "SELECT * FROM Student ORDER BY Marks DESC"
# query = "SELECT * FROM Student WHERE City='Ahmedabad' or City='Surat'
# query = "SELECT * FROM Student WHERE Marks >80 and Course='BCA'"
# query = "SELECT * FROM Student WHERE Marks between 70 and 90

    query = "SELECT * FROM Student WHERE Name LIKE 'A%'"
    cur.execute(query)

    records = cur.fetchall()

    if records:
        for row in records:
            listbox.insert(END, row)
    else:
        listbox.insert(END, "No Record Found")

    cur.close()
    con.close()

Label(root, text="Students Whose Name Starts With A",
      font=("Arial",18,"bold")).pack(pady=10)

Button(root,text="Search",font=("Arial",12),
       command=search).pack()

listbox = Listbox(root,width=90,height=15,font=("Arial",11))
listbox.pack(pady=20)

root.mainloop()