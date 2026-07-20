from tkinter import*

root=Tk()

root.title("TKINTER Exmaple 2")
root.geometry("500x500")
root.configure(bg="aqua")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

font_style=("Times New Roman",15,"bold")

lbl_fname_title=Label(root,text="Enter First Name:",font=font_style)
lbl_fname_title.grid(row=0,column=0)

lbl_fname=Entry(root,width=20)
lbl_fname.grid(row=0,column=1)

lbl_lname_title=Label(root,text="Enter Last Name:",font=font_style)
lbl_lname_title.grid(row=1,column=0)

lbl_lname=Entry(root,width=20)
lbl_lname.grid(row=1,column=1)

lbl_address_title=Label(root,text="Enter Address:",font=font_style)
lbl_address_title.grid(row=2,column=0)

lbl_address=Entry(root,width=20)
lbl_address.grid(row=2,column=1)

lbl_roll_title=Label(root,text="Enter Roll Number:",font=font_style)
lbl_roll_title.grid(row=3,column=0)

lbl_roll=Entry(root,width=20)
lbl_roll.grid(row=3,column=1)

lbl_marks_title=Label(root,text="Enter Marks:",font=font_style)
lbl_marks_title.grid(row=4,column=0)

lbl_marks=Entry(root,width=20)
lbl_marks.grid(row=4,column=1)

lbl_submit=Button(root,text="Submit",font=font_style)
lbl_submit.grid(row=5,column=0)

root.mainloop()