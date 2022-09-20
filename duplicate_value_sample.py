from tkinter import *
from collections import Counter

root=Tk()
root.geometry("1000x700")
root.title("DUPLICATE VALUE FINDOUT SYSTEM")
root.resizable(False,False)

def enter():
    t.insert(END,c1.get())
    

def duplicate():
    root1=Tk()
    root1.geometry("1000x700")
    root1.title("DUPLICATE VALUE ")
    root1.resizable(False,False)
    t1=Text(root1,font=("Lucida Calligraphy",25,"bold"),width=42,height=9 )
    t1.place(x=0,y=106)
    v=str(c1.get())
    w=v.split()
    a=Counter(w)
    
    
    t1.insert(END,a)



def duplicate_sentence():
    root2=Tk()
    root2.geometry("1000x700")
    root2.title("DUPLICATE SENTENCE")
    root2.resizable(False,False)

    t2=Text(root2,font=("Lucida Calligraphy",25,"bold"),width=42,height=10 )
    t2.place(x=0,y=106)
    v=str(c1.get())
    w=v.split('.')
    x=Counter(w)

    t2.insert(END,x)

    

def RESET():
    t.delete("1.0",END)
    c1.set("")

Label(text="DUPILCATE STRING FINDOUT SYSTEM",bg="black",fg="white",font=("arial",33),width="300",height="2").pack()

t=Text(root,font=("Lucida Calligraphy",28,"bold"),width=38,height=7 )
t.place(x=0,y=250)

c1=StringVar()


e=Entry(font=("arial",40,"bold"),fg="black",bg="lightgreen",textvariable=c1).place(x=200,y=106)
#button

b1=Button(text="DUPLICATE WORD",font=("arial",15,"bold"),fg="black",bg="red",command=duplicate)
b1.place(x=50,y=600)
b2=Button(text="DUPLICATE SENTENCE",font=("arial",15,"bold"),fg="black",bg="red",command=duplicate_sentence)
b2.place(x=340,y=600)
b3=Button(text="CLOSE",font=("arial",15,"bold"),fg="black",bg="red",command=root.destroy)
b3.place(x=870,y=600)
b4=Button(text="RESET",font=("arial",15,"bold"),fg="black",bg="red",command=RESET)
b4.place(x=700,y=600)
b5=Button(text="ENTER",font=("arial",15,"bold"),fg="black",bg="red",command=enter)
b5.place(x=450,y=190)



root.mainloop()




























