class Library:
    def __init__(self,list,name):
        self.bookList=list
        self.name=name
        self.listDict={}

    def displayBook(self):
        print(f"We have following book in {self.name}")
        for book in self.bookList:
            print(book)

    def takeBook(self,user,book):
        if book not in self.listDict.keys():
              self.listDict.update({book:user})
              print("Lender-book database has been updated.You can take this book now")
        else:
            print(f"Book is already has been taken by {self.listDict[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been added  in the book list")

    def returnBook(self,book):
        self.listDict.pop(book)



if __name__=='__main__':
    user1=Library(['Python','Java','C++','C','JavaScript','Android'],"StudentLibrary")
    while(True):
        print(f"Welcome in {user1.name}\nEnter your choice")
        print("1.Display Books")
        print("2.Lend a Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice=input()
        if user_choice not in  ['1','2','3','4']:
            print("Please enter only integer values")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            user1.displayBook()
        elif user_choice==2:
            user=input("Enter user name:")
            book=input("Enter book name")
            user1.takeBook(user,book)
        elif user_choice==3:
            book=input("Enter the book name which you want to add in the list")
            user1.addBook(book)
        elif user1==4:
            book=input("Enter the book name which you want to return")
            user1.returnBook(book)
        else:
            print("Invalid option")

        print("Enter q for quite and c for Continue")
        user_choice1=input()
        while user_choice1!='q'and user_choice1!='c':
            continue
            if user_choice1=='q':
                exit()
            elif user_choice1=='c':
                continue
