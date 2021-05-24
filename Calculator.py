# class Comprehension:
#
#     def setComprehension(self,list1):
#         set=()=list1
#         print(f"The value are printing in set Comprehension formate: ",set)
#     def dictComprehension(self):
#         pass
#     def listComprehension(self):
#         pass
#
#
# user=Comprehension()
# enterNo = int(input("Enter the no of list values:\n"))
# print("Enter the value\n")
# for i in range(enterNo):
#     list1 = [(input("Enter the value: "))]
# print("1.Disctionary Comprehension\n2.Set Comprehension\n3.List Comprehension")
# value=int(input("Enter one of these values which are given above\n"))
# if value==1:
#     user.dictComprehension()
# elif value==2:
#     user.setComprehension()
# elif value==3:
#     user.listComprehension()
# else:
#     print("Enter correct options\n")


from tkinter import*
# From here start Tkinter tutorial
def button_Push(event):
    global screen
    text=event.widget.cget("text")
    if text=="=":
        if Get.get().isdigit():
            val=int(Get.get())
        else:
            val=eval(Get.get())
        Get.set(val)
        screen.update()
    elif text=="C":
         Get.set("")
         screen.update()
    else:
        Get.set(Get.get()+text)
        screen.update()
window=Tk()
window.geometry("173x250")
window.title("AMS CALCULATOR")
window.resizable(0,0)

Get=StringVar()
Get.set("")
screen=Entry(window,textvar=Get,bg='white',font="Lucida 18 ",fg='black',bd=2)
screen.place(x=1,y=1,height=30,width=168)

btn1=Button(window,text='1',bg='white',fg='blue',font="Lucida 10 bold")
btn1.place(x=2,y=39,height=30,width=40)
btn1.bind("<Button-1>",button_Push)

btn2=Button(window,text='2',bg='white',fg='blue',font="Lucida 10 bold")
btn2.place(x=42,y=39,height=30,width=40)
btn2.bind("<Button-1>",button_Push)

btn3=Button(window,text='3',bg='white',fg='blue',font="Lucida 10 bold")
btn3.place(x=82,y=39,height=30,width=40)
btn3.bind("<Button-1>",button_Push)

btnP=Button(window,text='+',bg='white',fg='blue',font="Lucida 10 bold")
btnP.place(x=130,y=39,height=30,width=40)
btnP.bind("<Button-1>",button_Push)

btn4=Button(window,text='4',bg='white',fg='blue',font="Lucida 10 bold")
btn4.place(x=2,y=69,height=30,width=40)
btn4.bind("<Button-1>",button_Push)

btn5=Button(window,text='5',bg='white',fg='blue',font="Lucida 10 bold")
btn5.place(x=42,y=69,height=30,width=40)
btn5.bind("<Button-1>",button_Push)

btn6=Button(window,text='6',bg='white',fg='blue',font="Lucida 10 bold")
btn6.place(x=82,y=69,height=30,width=40)
btn6.bind("<Button-1>",button_Push)

btnM=Button(window,text='-',bg='white',fg='blue',font="Lucida 10 bold")
btnM.place(x=130,y=69,height=30,width=40)
btnM.bind("<Button-1>",button_Push)

btn7=Button(window,text='7',bg='white',fg='blue',font="Lucida 10 bold")
btn7.place(x=2,y=99,height=30,width=40)
btn7.bind("<Button-1>",button_Push)

btn8=Button(window,text='8',bg='white',fg='blue',font="Lucida 10 bold")
btn8.place(x=42,y=99,height=30,width=40)
btn8.bind("<Button-1>",button_Push)

btn9=Button(window,text='9',bg='white',fg='blue',font="Lucida 10 bold")
btn9.place(x=82,y=99,height=30,width=40)
btn9.bind("<Button-1>",button_Push)

btnMl=Button(window,text='*',bg='white',fg='blue',font="Lucida 10 bold")
btnMl.place(x=130,y=99,height=30,width=40)
btnMl.bind("<Button-1>",button_Push)

btn0=Button(window,text='0',bg='white',fg='blue',font="Lucida 10 bold")
btn0.place(x=2,y=129,height=30,width=40)
btn0.bind("<Button-1>",button_Push)

btnE=Button(window,text='%',bg='white',fg='blue',font="Lucida 10 bold")
btnE.place(x=42,y=129,height=30,width=40)
btnE.bind("<Button-1>",button_Push)

btnD=Button(window,text='.',bg='white',fg='blue',font="Lucida 10 bold")
btnD.place(x=82,y=129,height=30,width=40)
btnD.bind("<Button-1>",button_Push)

btnDv=Button(window,text='/',bg='white',fg='blue',font="Lucida 10 bold")
btnDv.place(x=130,y=129,height=30,width=40)
btnDv.bind("<Button-1>",button_Push)


btnC=Button(window,text='=',bg='white',fg='blue',font="Lucida 10 bold")
btnC.place(x=10,y=189,height=30,width=75)
btnC.bind("<Button-1>",button_Push)

btnC=Button(window,text='C',bg='white',fg='blue',font="Lucida 10 bold")
btnC.place(x=85,y=189,height=30,width=75)
btnC.bind("<Button-1>",button_Push)

footer=Label(window,text='Contact. Mr.Ajay Kumar 7524854091',fg='purple',font="Lucida 7 bold italic",bg='white')
footer.place(x=0,y=230)
window.mainloop()

