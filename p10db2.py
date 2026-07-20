from tkinter import *
import mysql.connector

root = Tk()
root.title("Student Record Search")
root.geometry("500x400")

def search():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="smit2007",
        database="CollegeDB"
    )

    cur = con.cursor()

    Roll_No = txt_roll.get()

    query = f"SELECT * FROM Student WHERE Roll_No={Roll_No}"
    cur.execute(query)

    record = cur.fetchone()

    if record:
        lbl_roll_value.config(text=record[0])
        lbl_name_value.config(text=record[1])
        lbl_age_value.config(text=record[2])
        lbl_gender_value.config(text=record[3])
        lbl_course_value.config(text=record[4])
        lbl_city_value.config(text=record[5])
        lbl_marks_value.config(text=record[6])
    else:
        lbl_roll_value.config(text="Not Found")
        lbl_name_value.config(text="")
        lbl_age_value.config(text="")
        lbl_gender_value.config(text="")
        lbl_course_value.config(text="")
        lbl_city_value.config(text="")
        lbl_marks_value.config(text="")

    cur.close()
    con.close()

Label(root, text="Student Record Search", font=("Arial", 18, "bold")).pack(pady=10)

Frame1 = Frame(root)
Frame1.pack(pady=10)

Label(Frame1, text="Enter Roll No:", font=("Arial", 12)).grid(row=0, column=0)

txt_roll = Entry(Frame1, font=("Arial", 12))
txt_roll.grid(row=0, column=1, padx=10)

Button(root, text="Search", font=("Arial", 12), command=search).pack(pady=10)

Frame2 = Frame(root)
Frame2.pack(pady=20)

Label(Frame2, text="Roll No:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky=W)
lbl_roll_value = Label(Frame2, font=("Arial", 12))
lbl_roll_value.grid(row=0, column=1, sticky=W)

Label(Frame2, text="Name:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky=W)
lbl_name_value = Label(Frame2, font=("Arial", 12))
lbl_name_value.grid(row=1, column=1, sticky=W)

Label(Frame2, text="Age:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky=W)
lbl_age_value = Label(Frame2, font=("Arial", 12))
lbl_age_value.grid(row=2, column=1, sticky=W)

Label(Frame2, text="Gender:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky=W)
lbl_gender_value = Label(Frame2, font=("Arial", 12))
lbl_gender_value.grid(row=3, column=1, sticky=W)

Label(Frame2, text="Course:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky=W)
lbl_course_value = Label(Frame2, font=("Arial", 12))
lbl_course_value.grid(row=4, column=1, sticky=W)

Label(Frame2, text="City:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky=W)
lbl_city_value = Label(Frame2, font=("Arial", 12))
lbl_city_value.grid(row=5, column=1, sticky=W)

Label(Frame2, text="Marks:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky=W)
lbl_marks_value = Label(Frame2, font=("Arial", 12))
lbl_marks_value.grid(row=6, column=1, sticky=W)

root.mainloop()