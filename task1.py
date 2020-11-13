#!python3
import tkinter as tk 
from tkinter import *

from tkinter import ttk

mywindow= tk.Tk()
mywindow.title("tk")
mywindow.geometry("600x50")
input1 = tk.Entry(mywindow,text="", width=30,)
lable1= tk.Label(mywindow,text="x")
input2 = tk.Entry(mywindow,text="", width=30,)
lable2= tk.Label(mywindow,text="=")
input3 = tk.Entry(mywindow,text="", width=50,)

input1.pack(side=LEFT)
lable1.pack(side=LEFT)
input2.pack(side=LEFT)
lable2.pack(side=LEFT)
input3.pack(side=LEFT)
mywindow.mainloop()