from tkinter import*
def click():
    print(f"Welcome Mr. {username.get()}\n Your data is succesfully submited")
    with open("recods.txt","a") as f:
         f.write(f"Entry_No: {userEntry.get()}\nUser_Name: {username}\nFather/Hushband_Name: {userpassword.get()}\nUser_Address: {useraddress.get()}\nUser_Mobile: {usermob.get()}\nUser_Member: {usermember.get()}\nPaid Amount: {useramount.get()}\n\n\n")


window=Tk()
window.geometry("450x350")
window.title("FramePage")

userEntry=StringVar()
username=StringVar()
userpassword=StringVar()
useraddress=StringVar()
usermob=StringVar()
usermember=StringVar()
useramount=StringVar()
tick=IntVar()

frame=Frame(window,bg='teal')
frame.place(x=0,y=0,height=50,width=450)

info=Label(frame,text='WELCOME IN TRAVELLING REGISTRATION FORM',bg='teal',fg='red',font=('',13,'bold'))
info.place(x=20,y=10)

entry=Label(window,text='Entry_No: ',font=('',10,'bold'))
entry.place(x=10,y=70)
userentry1=Entry(window,textvariable=userEntry,bg='lightgray',fg='black',font=('',12))
userentry1.place(x=175,y=70,width=50)

name=Label(window,text="User_name: ",font=('',10,'bold'))
name.place(x=10,y=95)
name1=Entry(window,textvariable=username,bg='lightgray',fg='black',font=('',12))
name1.place(x=175,y=95,width=250)


father=Label(window,text='Father/Hushband_name: ',font=('',10,'bold'))
father.place(x=10,y=120)
userpassword1=Entry(window,textvariable=userpassword,bg='lightgray',fg='black',font=('',12,''))
userpassword1.place(x=175,y=120,width=250)


address=Label(window,text="User_address: ",font=('',10,'bold'))
address.place(x=10,y=145)
useraddress1=Entry(window,textvariable=useraddress,bg='lightgray',fg='black',font=('',12))
useraddress1.place(x=175,y=145,width=250)

mobile=Label(window,text="User_Mobile: ",font=('',10,'bold'))
mobile.place(x=10,y=170)
usermob1=Entry(window,textvariable=usermob,bg='lightgray',fg='black',font=('',12))
usermob1.place(x=175,y=170,width=250)

member=Label(window,text="User_Member's : ",font=('',10,'bold'))
member.place(x=10,y=195)
usermember1=Entry(window,textvariable=usermember,bg='lightgray',fg='black',font=('',12))
usermember1.place(x=175,y=195,width=250)

amount=Label(window,text="Payble_Amount_By_The_User:      Rs=",font=('',10,'bold'))
amount.place(x=10,y=220)
useramount1=Entry(window,textvariable=useramount,bg='lightgray',fg='black',font=('',12))
useramount1.place(x=265,y=220,width=160)



tick1=Checkbutton(window,text='Do you pay amount by online?',variable=tick)
tick1.place(x=80,y=270)

submit=Button(window,text='Submit',bg='Green',fg='black',command=click)
submit.place(x=280,y=270,height=30,width=130)


window.mainloop()