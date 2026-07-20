from tkinter import *
operator=""

def add():
    global operator
    operator="+"

def sub():
    global operator
    operator="-"

def mul():
    global operator
    operator="*"

def div():
    global operator
    operator="/"
   

def equal():
    no1=int(lbl_no1.get())
    no2=int(lbl_no2.get())

    if(operator=="+"):
        number.set(no1+no2)
    elif(operator=="-"):
        number.set(no1-no2)
    elif(operator=="*"):
        number.set(no1*no2)
    elif(operator=="/"):
        number.set(no1/no2)


root = Tk()
root.title("Calculator")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

font_style = ("Arial", 14)
button_font = ("Arial", 14, "bold")

frame = Frame(root, bg="#f0f0f0")
frame.pack(expand=True)


number=StringVar()
title = Label(
    frame,
    text="Simple Calculator",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0"
)
title.grid(row=0, column=0, columnspan=2, pady=15)

lbl_no1_title = Label(
    frame,
    text="Enter Number 1:",
    font=font_style,
    bg="#f0f0f0"
)
lbl_no1_title.grid(row=1, column=0, padx=10, pady=5, sticky="w")

lbl_no1 = Entry(frame, width=20, font=font_style)
lbl_no1.grid(row=1, column=1, padx=10, pady=5)

lbl_no2_title = Label(
    frame,
    text="Enter Number 2:",
    font=font_style,
    bg="#f0f0f0"
)
lbl_no2_title.grid(row=2, column=0, padx=10, pady=5, sticky="w")

lbl_no2 = Entry(frame, width=20, font=font_style)
lbl_no2.grid(row=2, column=1, padx=10, pady=5)

lbl_add = Button(frame, text="+", font=button_font, width=8, command=add)
lbl_add.grid(row=3, column=0, padx=5, pady=5)

lbl_sub = Button(frame, text="-", font=button_font, width=8,command=sub)
lbl_sub.grid(row=3, column=1, padx=5, pady=5)

lbl_mul = Button(frame, text="×", font=button_font, width=8,command=mul)
lbl_mul.grid(row=4, column=0, padx=5, pady=5)

lbl_div = Button(frame, text="÷", font=button_font, width=8,command=div)
lbl_div.grid(row=4, column=1, padx=5, pady=5)

lbl_equal = Button(frame, text="=", font=button_font, width=18, command=equal)
lbl_equal.grid(row=5, column=0, columnspan=2, pady=10)

lbl_result_title = Label(
    frame,
    text="Answer:",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0"
)
lbl_result_title.grid(row=6, column=0, pady=10)

lbl_result = Label(
    frame,
    text="",
    font=("Arial", 14),
    bg="white",
    width=15,
    relief="sunken",
    textvariable=number
)
lbl_result.grid(row=6, column=1)

root.mainloop()