from tkinter import *
import random

number=0
root = Tk()
root.title("Snake and Ladder")

player=StringVar()
dice=StringVar()
won=StringVar()
no = 1
i,p1,p2=1,1,1

def p1snake_ladder():
    global p1
    ladders = {4: 25,13: 46,33: 49,42: 63,50: 69,62: 81,74: 92}
    snakes = {98: 78,95: 56,88: 24,64: 60,48: 26,36: 6,32: 10}

    if(p1 in ladders):
        p1=ladders[p1]
        won.set("p1-Climbed Ladder")
    elif(p1 in snakes):
        p1=snakes[p1]
        won.set("p1-Bite By Snake")

def p2snake_ladder():
    global p2
    ladders = {4: 25,13: 46,33: 49,42: 63,50: 69,62: 81,74: 92}
    snakes = {98: 78,95: 56,88: 24,64: 60,48: 26,36: 6,32: 10}

    if(p2 in ladders):
        p2=ladders[p2]
        won.set("p2-Climbed Ladder")
    elif(p2 in snakes):
        p2=snakes[p2]
        won.set("p2-Bite By Snake")

def roll_dice():
    global i,p1,p2
    global number
    number=random.randint(1,6)
    dice.set(number)
    
    if(i==1):
        player.set("P1")
        if(p1+number<=100):
            won.set("")
            buttons[p1].config(bg="SystemButtonFace",text=str(p1))
            p1+=number
            p1snake_ladder()
            buttons[p1].config(bg="red",text="P1")
            i=2
        if(p1==100):
            won.set("Player 1 Won")
            lbl_btn_dice.config(state=DISABLED)

    elif(i==2):
        won.set("")
        player.set("P2")
        if(p2+number<=100):
            buttons[p2].config(bg="SystemButtonFace",text=str(p2))
            p2+=number
            p2snake_ladder()
            buttons[p2].config(bg="blue",text="P2")
            i=1
        if(p2==100):
            won.set("Player 2 Won")
            lbl_btn_dice.config(state=DISABLED)
        

buttons=[None]*101
    
for row in range(9, -1, -1):

    # Bottom row, then every alternate row goes left to right
    if (9 - row) % 2 == 0:
        for col in range(10):
            btn = Button(root, text=str(no), width=5, height=2)
            btn.grid(row=row, column=col)
            buttons[no]=btn
            no += 1

    # Other rows go right to left
    else:
        for col in range(9, -1, -1):
            btn = Button(root, text=str(no), width=5, height=2)
            btn.grid(row=row, column=col)
            buttons[no]=btn
            no += 1


lbl_btn_dice=Button(root,text="Roll",command=roll_dice)
lbl_btn_dice.grid(row=10,column=0)

lbl_dice_title=Label(root,text="Dice")
lbl_dice_title.grid(row=11,column=0)

lbl_dice=Label(root,width=5,textvariable=dice)
lbl_dice.grid(row=11,column=1)

lbl_player=Label(root,text="Player:")
lbl_player.grid(row=11,column=2)

lbl_player=Label(root,width=5,textvariable=player)
lbl_player.grid(row=11,column=3)

lbl_winner=Label(root,text="Winner:")
lbl_winner.grid(row=12,column=0)

lbl_winner=Label(root,width=16,textvariable=won,font=(15),fg="green")
lbl_winner.grid(row=12,column=1,columnspan=5)

root.mainloop()