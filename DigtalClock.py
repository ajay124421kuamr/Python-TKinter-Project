# # import json
# # data='{"var1":"Mohan","var2":"Rakesh","var3":"Rohan"}'
# # parse=json.load(data)
# # print(parse)
# #
# # # data2 = {"car":['bmw','Ferrari','honda city'],"Language":('python','c','java','android')}
# # # jumped=json.dumps(sort_keys=data2)
# # # print(jumped)
# import random
# class Bank:
#
#     def registerUser(self,type,name,acc,mob,add,amount):
#         print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:- STATE BANK OF INDIA USER REGISTRATION WINDOW -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
#
#         print(f"Account Type: {type}\nCustomer Name: {name}\nCustomer Account No: {acc}\nCustomer Mobile No: {mob}\nCustomer Address: {add}\nCustomer Account Opening Balance: {amount}")
#
#     def balanceEnquiry(self,amount):
#         print(
#             "-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:- STATE BANK OF INDIA BALANCE ENQUIRY -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
#         if amount==0:
#            raise ValueError("Amount is not defined...")
#         else:
#            print(f"Your availble balanace is: {amount}")
#         print("\n\t\t\tThank''s for using our software\n")
#
#     def withdrawalAmount(self,amount):
#         print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:- STATE BANK OF INDIA AMOUNT WITHDRAW WINDOW -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
#         amount1 = int(input("Enter your withdraw amount\n"))
#         if amount < amount1:
#                 print("Insufficient balance in your account\n")
#         else:
#                 print("Transaction succesfully done\n")
#                 amount = amount - amount1
#                 print(f"Your availble balance is: {amount} \n\t\t\tThank's for using our software\n")
#
#     def depositeAmount(self,amount):
#         print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:- STATE BANK OF INDIA AMOUNT DEPOSITE WINDOW -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
#         amount2 = int(input("Enter your amount to be deposte\n"))
#         amount = amount + amount2
#         print(f"Your availble balance is: {amount} \n\t\t\tThank's for using our software\n")
#
#     def Exit(self):
#         exit()
#
# user1=Bank()
# userName="rameshsingh"
# passwrd="yogibaba@123"
# print(
#     "-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:- STATE BANK OF INDIA USER LOGIN WINDOW -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
#
# u=input("Enter your Account UserName\n")
# p=input("Enter your Account Password\n")
# if u==userName and p==passwrd:
#     while True:
#         print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:- STATE BANK OF INDIA -:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
#         print("1.Open Account\n2.Balance Enquiry\n3.Amount withdraw\n4.Amount Desosite\n5.Exit\n")
#         select=int(input("Enter your selected value:\n"))
#         if (select==1):
#             type=input("Enter your account type\n")
#             name=input("Enter customer name:\n")
#             acc=int(input("Enter customer account no.\n"))
#             mob=int(input("Enter customer mobile no.\n"))
#             add=input("Enter customer address\n")
#             amount=int(input("Enter account opening amount\n"))
#             user1.registerUser(type,name,acc,mob,add,amount)
#         elif select==2:
#               user1.balanceEnquiry(amount)
#         elif select==3:
#             user1.withdrawalAmount(amount)
#         elif select==4:
#             user1.withdrawalAmount(amount)
#         elif select==5:
#             user1.Exit()
# else:
#     print("Your UserName or UserPassword is Incorrect.Please Enter correct Detail's Thank's\n\n")
#

#Creating user login form
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
