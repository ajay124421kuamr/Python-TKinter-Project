import random
list1=["s","g","w"]
human_score=0
computer_score=0
chance=10
no_of_chance=0
print("Snake, Water, Gun Game")
print("\tpress key: 'S' for snake\n\tpress key: 'W' for water\n\tpress key: 'G' for gun\n")
while no_of_chance<chance:
    string=input("Enter your value\n")
    _random=random.choice(list1)
    if string==_random:
        print("Tie Both 0 point to each\n")
    elif string=='s'and _random=='g':
        computer_score=computer_score+1
        print(f"your guess is {string} and computer guess is {_random}\n")
        print("computer win 1 point\n")
        print(f"computer points is: {computer_score} and your points is: {human_score}\n")
    elif string=='s'and _random=='w':
        human_score=human_score+1
        print(f"your guess is {string} and computer guess is {_random}\n")
        print("you win 1 point\n")
        print(f"your point is {human_score} and computer points is {computer_score}\n")
    elif string=='w'and _random=='s':
        computer_score=computer_score+1
        print(f"you guess {string} and computer guess {_random}\n")
        print("computer win 1 point\n")
        print(f"computer points is {computer_score} and your points is {human_score}\n")
    elif str=='w'and _random=='g':
        human_score=human_score+1
        print(f"you guess {string} and computer guess {_random}\n")
        print("you win 1 point\n")
        print(f"computer points is: {computer_score} and your points is {human_score}\n")
    elif string=='g'and _random=='s':
        human_score=human_score+1
        print(f"you guess {string} and computer guess {_random}\n")
        print("you win 1 point\n")
        print(f"computer points is: {computer_score} and your points is: {human_score}\n")
    elif string=='g'and _random=='w':
        computer_score=computer_score+1
        print(f"you guess {string} and computer guess {_random}\n")
        print("computer win 1 point\n")
        print(f"compputer points is {computer_score} and your points is: {human_score}\n")
    else:
        print("you have enter wrong input\n")
    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")
print("Game over\n")
if computer_score==human_score:
     print("Tie\n")
elif computer_score>human_score:
    print(f"Computer score is: {computer_score} so computer is winnner\n")
else:
    print(f"Your score is: {human_score} so you are winner\n")
print("Thanks to play with me...")