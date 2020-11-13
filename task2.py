#!python3
import tkinter as tk 
from tkinter import *

from tkinter import ttk

mywindow= tk.Tk()
mywindow.title("T-Town Vetrinary Clinic Database")
mywindow.geometry("600x400")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(mywindow, image=dogphoto)
input1 = tk.Entry(mywindow,text="", width=30)
button1 = tk.Button(mywindow,text="Search By Name")
lable2= tk.Label(mywindow,text="Client Database",width=30)

prev= tk.Button(mywindow,text="Previous",width=30)
nextb= tk.Button(mywindow,text="Next",width=30)
save= tk.Button(mywindow,text="Save",width=30)

inputa = tk.Entry(mywindow,text="", width=30)
inputb = tk.Entry(mywindow,text="", width=30)
inputc = tk.Entry(mywindow,text="", width=30)
inputd = tk.Entry(mywindow,text="", width=30)
inpute = tk.Entry(mywindow,text="", width=30)

name= tk.Label(mywindow,text="name",width=30)
typel= tk.Label(mywindow,text="type",width=30)
breed= tk.Label(mywindow,text="breed",width=30)
owner= tk.Label(mywindow,text="owner",width=30)
birthday= tk.Label(mywindow,text="birthday",width=30)







label1.grid(row=1,column=1,rowspan=2)
input1.grid(row=1,column=5)
button1.grid(row=1,column=4)
lable2.grid(row=2,column=3)

prev.grid(row=5,column=1)
nextb.grid(row=5,column=5)
save.grid(row=5,column=3)

name.grid(row=3,column=1)
typel.grid(row=3,column=2)
breed.grid(row=3,column=3)
owner.grid(row=3,column=4)
birthday.grid(row=3,column=5)

inputa.grid(row=4,column=1)
inputb.grid(row=4,column=2) 
inputc.grid(row=4,column=3) 
inputd.grid(row=4,column=4) 
inpute.grid(row=4,column=5)




mywindow.mainloop()