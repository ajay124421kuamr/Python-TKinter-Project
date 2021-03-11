from tkinter import * #import tkinter module
from PIL import Image, ImageTk #import pillow module

#Creating fuction to implement all operations
def click(event):
    global Value
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if Value.get().isdigit():
            value=int(Value.get())
        else:
             value=eval(Value.get())
        Value.set(value)
        Screen.update()
    elif text=="clear":
        Value.set("")
        Screen.update()

    else:
        Value.set(Value.get()+text)
        Screen.update()

# crating root of the window
windows=Tk()

#setting the geometry of window
windows.geometry("470x370")

#set the title of the window
windows.title("Simple Calculator by Ajay kumar")

# set the resizable to 0 0
windows.resizable(0,0)

#Set the icon on the window
windows.wm_iconbitmap("ams.bmp")

# windows.minsize(250,300) # setting the mimimun size of the windows
# windows.maxsize(750,650) #setting the maximum size of the windows

#For jpg images
Iname=Image.open("audi.jpg")
source=ImageTk.PhotoImage(Iname)
photo=Label(image=source)
photo.pack()

# creating the frame on the windows
frame=Frame(windows).pack()

#setting the label on the frame with place
info=Label(frame,text='WELCOME IN MY SIMPLE CALCULATOR',bg='teal',fg='white',font=('lucida',17,'bold'))
info.place(x=0,y=0,height=40,width=470)

#Createing subLabel
subinfo=Label(frame,text='Contact developer. Mr.AjayKumar [7524854091 ,ak4995319@gmail.com]',font="lucida 10 bold",bg='white',fg='red')
subinfo.place(x=5,y=40,width=460)

#Creating Value variable for get Value from the label
Value=StringVar()
Value.set("")
Screen=Entry(frame,textvar=Value,bg='lightgray',font=('Lucida',30,'bold'))
Screen.place(x=10,y=62,height=60,width=450)


#Creating buttons for the opee=rations on the frame
one=Button(frame,text='1',bg='cyan',fg='red',font=('',15,''))
one.place(x=10,y=210,height=40,width=90)
one.bind("<Button-1>",click)


two=Button(frame,text='2',bg='cyan',fg='red',font=('',15,''))
two.place(x=100,y=210,height=40,width=90)
two.bind("<Button-1>",click)

three=Button(frame,text='3',bg='cyan',fg='red',font=('',15,''))
three.place(x=190,y=210,height=40,width=90)
three.bind("<Button-1>",click)

four=Button(frame,text='4',bg='cyan',fg='red',font=('',15,''))
four.place(x=280,y=210,height=40,width=90)
four.bind("<Button-1>",click)

five=Button(frame,text='5',bg='cyan',fg='red',font=('',15,''))
five.place(x=370,y=210,height=40,width=90)
five.bind("<Button-1>",click)

six=Button(frame,text='6',bg='cyan',fg='red',font=('',15,''))
six.place(x=10,y=250,height=40,width=90)
six.bind("<Button-1>",click)

seven=Button(frame,text='7',bg='cyan',fg='red',font=('',15,''))
seven.place(x=100,y=250,height=40,width=90)
seven.bind("<Button-1>",click)

eight=Button(frame,text='8',bg='cyan',fg='red',font=('',15,''))
eight.place(x=190,y=250,height=40,width=90)
eight.bind("<Button-1>",click)

nine=Button(frame,text='9',bg='cyan',fg='red',font=('',15,''))
nine.place(x=280,y=250,height=40,width=90)
nine.bind("<Button-1>",click)

zero=Button(frame,text='0',bg='cyan',fg='red',font=('',15,''))
zero.place(x=370,y=250,height=40,width=90)
zero.bind("<Button-1>",click)

plus=Button(frame,text='+',bg='cyan',fg='red',font=('',15,''))
plus.place(x=10,y=290,height=40,width=90)
plus.bind("<Button-1>",click)

minus=Button(frame,text='-',bg='cyan',fg='red',font=('',15,''))
minus.place(x=100,y=290,height=40,width=90)
minus.bind("<Button-1>",click)

multi=Button(frame,text='*',bg='cyan',fg='red',font=('',15,''))
multi.place(x=190,y=290,height=40,width=90)
multi.bind("<Button-1>",click)

devide=Button(frame,text='/',bg='cyan',fg='red',font=('',15,''))
devide.place(x=280,y=290,height=40,width=90)
devide.bind("<Button-1>",click)

per=Button(frame,text='%',bg='cyan',fg='red',font=('',15,''))
per.place(x=370,y=290,height=40,width=90)
per.bind("<Button-1>",click)


clear=Button(frame,text='clear',bg='cyan',fg='red',font=('',15,''))
clear.place(x=10,y=330,height=35,width=150)
clear.bind("<Button-1>",click)


equal=Button(frame,text='=',bg='cyan',fg='red',font=('',15,''))
equal.place(x=160,y=330,height=35,width=150)
equal.bind("<Button-1>",click)

dot=Button(frame,text='.',bg='cyan',fg='red',font=('',30,''))
dot.place(x=310,y=330,height=35,width=150)
dot.bind("<Button-1>",click)

windows.mainloop()