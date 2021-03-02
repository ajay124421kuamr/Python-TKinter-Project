#Creating Digital Clock with date and time
from tkinter import *
from tkinter.ttk import*
from time import strftime
root = Tk()
root.title("Didgital clock created by.@jayKumar")
root.resizable(0,0)
def time():
    string=strftime('%H:%M:%S:%p')
    str=strftime('-:-:-:-:-:-:-:-:-:-:-:- Date: %d/%m/20%y -:-:-:-:-:-:-:-:-:-:-:-\nContact AjayKumar.7524854091, ak4995319@gmail.com')
    label.config(text=string)
    label1.config(text=str)
    label.after(1000,time)
label=Label(root,font=("ds-digital",80),background="black",foreground="red")
label1=Label(root,font=("ds-digital",20),background="black",foreground="blue")
label.pack(anchor='center')
label1.pack(anchor='center')
time()
root.mainloop()
