from tkinter import*
import random

root=Tk()
root.title("Stone, Paper and scissor")
root.geometry("500x500")
cchoice=StringVar()
result=StringVar()

def check():
    global uchoice
    if(uchoice.get()==cchoice.get()):
        result.set("Draw")
    elif((uchoice.get()=="Paper" and cchoice.get()=="Stone") or (uchoice.get()=="Stone" and cchoice.get()=="Scissor") or (uchoice.get()=="Scissor" and cchoice.get()=="Paper")):
        result.set("User Won")
    else:
        result.set("Computer Won")

def play():
    option=["Stone","Scissor","Paper"]
    cchoice.set(random.choice(option))
    check()

uchoice=""
uchoice=StringVar()


def paper():
    global uchoice
    uchoice.set("Paper")
    play()

def stone():
    global uchoice
    uchoice.set("Stone")
    play()

def scissor():
    global uchoice
    uchoice.set("Scissor")
    play()


lbl_comp_choice=Label(root,text="Computer's Choice:")
lbl_comp_choice.grid(row=0,column=0)

lbl_comp=Entry(root,width=20,textvariable=cchoice)
lbl_comp.grid(row=0,column=1)

lbl_user_choice=Label(root,text="User's Choice:")
lbl_user_choice.grid(row=1,column=0)

lbl_user=Entry(root,width=20,textvariable=uchoice)
lbl_user.grid(row=1,column=1)

lbl_user_paper=Button(root,text="Paper",command=paper)
lbl_user_paper.grid(row=2,column=0)

lbl_user_stone=Button(root,text="Stone",command=stone)
lbl_user_stone.grid(row=2,column=1)

lbl_user_scissor=Button(root,text="Scissor",command=scissor)
lbl_user_scissor.grid(row=2,column=2)

lbl_resu=Label(root,text="Result")
lbl_resu.grid(row=3,column=0)

lbl_result=Entry(root,width=20,textvariable=result)
lbl_result.grid(row=3,column=1)
root.mainloop()