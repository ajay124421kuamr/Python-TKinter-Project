#Age calculator

print("\t\t\t\t\tWELCOME")
age=int(input("Enter your age or year of birth\n")) #take user input
cuYaer=2021 #assining value to cuYear varibale
year=100 #assining value to year variable 
if (len(str(age))==2): #check if age variable has 2 integer lenght
    print("You are enterd your age:") #print a message on the casole
    age1=(cuYaer-age)
    print(f"And your year of birth will: {age1} by you age")
    if age<=17:
        print(f"You are teen ager becouse your age is: {age}")
    elif age>=18:
        print(f"You are adult ager and you age is: {age}")

elif (len(str(age))==4):
    print("You are entered your year of birth")
    if age<cuYaer:
        age=cuYaer-age
        age1=year-age
        print(f"Your age is: {age} and now you have availble year to reach century: {age1}")
    elif age>cuYaer:
        print("You are not born yet.Please wait until you born in this world")


