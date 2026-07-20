from tkinter import*

def input():
    name=txt_name.get()
    name_var.set("Welcome "+ name)
    
    no=int(txt_number.get())
    square_var.set("Square: "+str(no*no))
    


root = Tk()
root.title("simple TKINTER Example")
root.geometry("500x500")

name_var=StringVar()
square_var=StringVar()

lbl_name=Label(root,text="Enter Name:")
lbl_name.grid(row=0,column=0)

lbl_number=Label(root,text="Enter number")
lbl_number.grid(row=1,column=0)

txt_number=Entry(root,width=20)
txt_number.grid(row=1,column=1)

txt_name=Entry(root,width=20)
txt_name.grid(row=0,column=1)

btn_submit=Button(root,text="Submit",command=input)
btn_submit.grid(row=2,column=0)

lbl_result_title1=Label(root,text="Name")
lbl_result_title1.grid(row=3,column=0)

lbl_result1=Label(root,textvariable=name_var)
lbl_result1.grid(row=3,column=1)

lbl_result_title2=Label(root,text="Answer")
lbl_result_title2.grid(row=4,column=0)

lbl_result2=Label(root,textvariable=square_var)
lbl_result2.grid(row=4,column=1)

root.mainloop()