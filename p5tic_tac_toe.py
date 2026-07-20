from tkinter import *
i=0

def disable_board():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def winner():

    if(btn1["text"]==btn2["text"]==btn3["text"] and btn1["text"]!=""):
        if(btn1["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()

    elif(btn4["text"]==btn5["text"]==btn6["text"] and btn4["text"]!=""):
        if(btn4["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()

    elif(btn7["text"]==btn8["text"]==btn9["text"] and btn7["text"]!=""):
        if(btn7["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()

    elif(btn1["text"]==btn4["text"]==btn7["text"] and btn1["text"]!=""):
        if(btn1["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()

    elif(btn2["text"]==btn5["text"]==btn8["text"] and btn2["text"]!=""):
        if(btn2["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()

    elif(btn3["text"]==btn6["text"]==btn9["text"] and btn3["text"]!=""):
        if(btn3["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()

    elif(btn1["text"]==btn5["text"]==btn9["text"] and btn1["text"]!=""):
        if(btn1["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()

    elif(btn3["text"]==btn5["text"]==btn7["text"] and btn3["text"]!=""):
        if(btn3["text"]=="X"):
            result.set("Winner X")
            disable_board()
        else:
            result.set("Winner O")
            disable_board()
    

def turn_check(b):
    global i

    if(b==1):
        if(btn1["text"]==""):
            i+=1
            if(i%2==0):
                btn1.config(text="X")
            else:
                btn1.config(text="O")
        winner()
    elif(b==2):
        if(btn2["text"]==""):
            i+=1
            if(i%2==0):
                btn2.config(text="X")
            else:
                btn2.config(text="O")
        winner()
    elif(b==3):
        if(btn3["text"]==""):
            i+=1
            if(i%2==0):
                btn3.config(text="X")
            else:
                btn3.config(text="O")
        winner()
    elif(b==4):
        if(btn4["text"]==""):
            i+=1
            if(i%2==0):
                btn4.config(text="X")
            else:
                btn4.config(text="O")
        winner()
    elif(b==5):
        if(btn5["text"]==""):
            i+=1
            if(i%2==0):
                btn5.config(text="X")
            else:
                btn5.config(text="O")
        winner()
    elif(b==6):
        if(btn6["text"]==""):
            i+=1
            if(i%2==0):
                btn6.config(text="X")
            else:
                btn6.config(text="O")
        winner()
    elif(b==7):
        if(btn7["text"]==""):
            i+=1
            if(i%2==0):
                btn7.config(text="X")
            else:
                btn7.config(text="O")
        winner()
    elif(b==8):
        if(btn8["text"]==""):
            i+=1
            if(i%2==0):
                btn8.config(text="X")
            else:
                btn8.config(text="O")
        winner()
    elif(b==9):
        if(btn9["text"]==""):
            i+=1
            if(i%2==0):
                btn9.config(text="X")
            else:
                btn9.config(text="O")
        winner()

root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")
root.configure(bg="#2c3e50")

result=StringVar()
# ✅ ADD THIS (makes all buttons large)
root.option_add("*Button.Font", ("Arial", 24, "bold"))
root.option_add("*Button.Width", 6)
root.option_add("*Button.Height", 3)

font_style = ("Arial", 24, "bold")

# Center frame
frame = Frame(root, bg="#2c3e50")
frame.place(relx=0.5, rely=0.5, anchor="center")


# Grid buttons
btn1 = Button(frame, command=lambda:turn_check(1)); btn1.grid(row=0, column=0, padx=5, pady=5)
btn2 = Button(frame, command=lambda:turn_check(2)); btn2.grid(row=0, column=1, padx=5, pady=5)
btn3 = Button(frame, command=lambda:turn_check(3)); btn3.grid(row=0, column=2, padx=5, pady=5)

btn4 = Button(frame, command=lambda:turn_check(4)); btn4.grid(row=1, column=0, padx=5, pady=5)
btn5 = Button(frame, command=lambda:turn_check(5)); btn5.grid(row=1, column=1, padx=5, pady=5)
btn6 = Button(frame, command=lambda:turn_check(6)); btn6.grid(row=1, column=2, padx=5, pady=5)

btn7 = Button(frame, command=lambda:turn_check(7)); btn7.grid(row=2, column=0, padx=5, pady=5)
btn8 = Button(frame, command=lambda:turn_check(8)); btn8.grid(row=2, column=1, padx=5, pady=5)
btn9 = Button(frame, command=lambda:turn_check(9)); btn9.grid(row=2, column=2, padx=5, pady=5)

lbl_result_title = Label(
    frame,
    font=("Arial", 20, "bold"),
    bg="#1abc9c",
    fg="white",
    textvariable=result,
    width=15,
    height=2,
    relief="solid",
    bd=3
)

lbl_result_title.grid(row=3, column=0, columnspan=3, pady=15)
root.mainloop()