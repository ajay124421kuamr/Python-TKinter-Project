#User Login Page using by tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("User Login System contact.7524854091 for more help by @jaykumar")
        self.root.geometry("1100x600+100+50")
        self.root.resizable(0,0)
        self.root=Label(bg='purple').place(x=0,y=0,height=600,width=1100)
        self.root=Label(bg='purple',text="STATE BANK OF INDIA ONLINE BANKING",fg='yellow',font=('ar',30,'bold','underline')).place(x=10,y=20,height=40,width=800)
        self.root=Label(bg='purple',text='Always One Step Forward For Information Technology And Serve Best Services To Customers',fg='yellow',font=('times new roman',12,'bold','underline','italic')).place(x=10,y=70)
        #Insert image
        self.bg=PhotoImage(file="555.jpeg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        #===Createting Frame===
        frame_login=Frame(self.root,bg='teal',bd=15).place(x=150,y=150,height=370,width=500)

        Frame_title=Label(frame_login,text="Login Here",font=('impact',35,'bold'),bg='teal',fg='orange').place(x=200,y=150)
        Frame_subtitle=Label(frame_login,text="State Bank Of India User Login Area",font=('Goudy old style',15,'bold'),bg='teal',fg='orange').place(x=200,y=210)

        #Creating User name and password label
        name= Label(frame_login, text="Username", font=('Goudy old style', 15, 'bold'),bg='teal', fg='orange').place(x=200, y=250)
        self.txt_user=Entry(frame_login,font=('times new roman',15),bg='lightgray')
        self.txt_user.place(x=200,y=280,height=30,width=390)

        password = Label(frame_login, text="Password", font=('Goudy old style', 15, 'bold'), bg='teal', fg='orange').place(x=200, y=330)
        self.txt_password = Entry(frame_login, font=('times new roman', 15), bg='lightgray')
        self.txt_password.place(x=200, y=360, height=30,width=390)

        forgot=Button(self.root,text='Forgot Password?',cursor='hand2',font=('times new roman',12),bg='teal',fg='orange',bd=0).place(x=195,y=420,height=20,width=120)

        login=Button(self.root,text='Login',cursor='hand2',font=('times new roman',15,'bold'),bg='orange',fg='white',command=self.userLogin).place(x=440,y=420,height=40,width=150)


    def userLogin(self):
        if self.txt_user.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        elif self.txt_user.get()!="Ramesh" or self.txt_password.get()!="123456":
            messagebox.showerror("Error","UserName/Password is incorrect",parent=self.root)

        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour password: {self.txt_password.get()}",parent=self.root)


root=Tk()
obj=Login(root)
root.mainloop()
