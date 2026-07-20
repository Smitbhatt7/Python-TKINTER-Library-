from tkinter import *
import mysql.connector

root=Tk()
root.title("Electrical Shop Project")
root.geometry("1000x1000")
root.configure(bg="white")

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="smit2007",
    database="electrical"
)

cur=con.cursor()

cart=None
btn=None
images=[]

def show_cart():
    global cart
    root.withdraw()
    cart=Toplevel()
    cart.title("Cart")
    cart.geometry("700x500")
    Label(cart,text="Cart",font=("Arial",20)).grid(row=0,column=0,pady=20)

    Button(cart,text="Home Page",width=15,command=home_page).grid(row=1,column=0)


def show_pro_cat():
    global pro_cat
    root.withdraw()
    pro_cat=Toplevel()
    pro_cat.title("Categories")
    pro_cat.geometry("1000x1000")
    Label(pro_cat,text="Categories",font=("Arial",20)).grid(row=0,column=0,pady=20)

    Button(pro_cat,text="Home Page",width=15,command=home_page).grid(row=1,column=0)


def home_page():
    root.deiconify()
    if(cart):
        cart.destroy()
    else:
        pro_cat.destroy()


def btn_press(id):
    global btn,images

    btn=id

    if(btn==1):
        query=f"select PName,PImg from Product WHERE CatID=1"
        cur.execute(query)
        switch=cur.fetchall()
        images.clear()

        r,c=1,4

        for PName,PImg in switch:
            img=PhotoImage(file=PImg)
            images.append(img)

            Button(
                root,
                text=PName,
                image=img,
                compound="top",
                width=200,
                height=200
            ).grid(row=r,column=c)

            c+=1
            if(c==8):
                r+=1
                c=0

Label(
    root,
    text="Electrical Shop Management",
    bg="#0B5394",
    fg="white",
    font=("Arial",20,"bold"),
    pady=10
).grid(row=0,column=0,columnspan=2,sticky="ew")


category_frame=Frame(root,bg="#ECECEC",bd=2,relief="ridge")
category_frame.grid(row=1,column=0,sticky="ns",padx=10,pady=10)

Label(
    category_frame,
    text="Categories",
    bg="#ECECEC",
    font=("Arial",15,"bold")
).grid(row=0,column=0,pady=10)

Button(category_frame,text="Product List",width=18,command=show_pro_cat).grid(row=1,column=0,pady=5)

r=2
query="SELECT CatID,CatName FROM Category"
cur.execute(query)
category=cur.fetchall()
for CatID,CatName in category:
    cat_btn=Button(
        category_frame,
        text=CatName,
        width=18,
        command=lambda id=CatID: btn_press(id)
    )

    cat_btn.grid(row=r,column=0,pady=5)
    r+=1

# Leave some space
Label(category_frame,bg="#ECECEC").grid(row=r,column=0,pady=20)

# Cart button at the bottom
Button(
    category_frame,
    text="🛒 Cart",
    width=18,
    bg="#0B5394",
    fg="white",
    font=("Arial",10,"bold"),
    command=show_cart
).grid(row=r+1,column=0,pady=10)
root.mainloop()

cur.close()
con.close()