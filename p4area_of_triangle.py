from tkinter import *

def input_output():
    base=int(lbl_base.get())
    height=int(lbl_height.get())

    answer.set((base*height/2))

root = Tk()
root.title("Area Of Triangle")
root.geometry("500x500")
root.configure(bg="#f4f6f8")

font_style = ("Segoe UI", 12)
title_font = ("Segoe UI", 18, "bold")

frame = Frame(root, bg="#f4f6f8")
frame.pack(expand=True)

answer=StringVar()

# Title
lbl_title = Label(
    frame,
    text="Area of Triangle",
    font=title_font,
    bg="#f4f6f8",
    fg="#2c3e50"
)
lbl_title.grid(row=0, column=0, columnspan=2, pady=20)

# Height
lbl_height_title = Label(
    frame,
    text="Enter Height:",
    font=font_style,
    bg="#f4f6f8"
)
lbl_height_title.grid(row=1, column=0, padx=10, pady=10, sticky="w")

lbl_height = Entry(
    frame,
    width=20,
    font=font_style
)
lbl_height.grid(row=1, column=1, padx=10, pady=10)

# Base
lbl_base_title = Label(
    frame,
    text="Enter Base:",
    font=font_style,
    bg="#f4f6f8"
)
lbl_base_title.grid(row=2, column=0, padx=10, pady=10, sticky="w")

lbl_base = Entry(
    frame,
    width=20,
    font=font_style
)
lbl_base.grid(row=2, column=1, padx=10, pady=10)

# Submit Button
lbl_submit = Button(
    frame,
    text="Calculate",
    font=font_style,
    bg="#3498db",
    fg="white",
    width=15,
    command=input_output
)
lbl_submit.grid(row=3, column=0, columnspan=2, pady=15)

# Result
lbl_result_title = Label(
    frame,
    text="Answer:",
    font=("Segoe UI", 12, "bold"),
    bg="#f4f6f8"
)
lbl_result_title.grid(row=4, column=0, pady=10)

lbl_result = Label(
    frame,
    text="",
    font=font_style,
    bg="white",
    width=15,
    relief="sunken",
    textvariable=answer
)
lbl_result.grid(row=4, column=1)

root.mainloop()