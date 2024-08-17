# Rock, Paper & Scissor Game:

# Rock -> 1
# Paper -> -1
# Scissor -> 0

import random

AI = random.choice([-1, 1, 0])

print("Welcome To Rock, Paper & Scissors!")
print("Reffer the Following to Play:")
print("r -> Rock\np -> Paper\ns -> Scissors\n")
User_Choice = input("Enter Your Choice: ")

User_Dict = {"r" : 1, "p" : -1, "s" : 0}
Choices = {1 : "Rock", -1 : "Paper", 0 : "Scissors"}
user = User_Dict[User_Choice]

print()
print(f"You Choose: {Choices[user]} \nComputer Choose: {Choices[AI]}")
print()
print("Game Result: ")

if(AI == user):
    print("Draw")
    print(f"{Choices[user]} vs {Choices[AI]}")
    print("No one Wins")
else:
    if(AI == 1 and user == -1):
        print("Congratulations! You Won...")
        print(f"{Choices[user]} vs {Choices[AI]}")
        print("Paper Wins!")

    elif(AI == 1 and user == 0):
        print("Oops!!! You Lose...")
        print(f"{Choices[user]} vs {Choices[AI]}")
        print("Rock Wins!")

    elif(AI == -1 and user == 0):
        print("Congratulations! You Won...")
        print(f"{Choices[user]} vs {Choices[AI]}")
        print("Scissor Wins!")

    elif(AI == -1 and user == 1):
        print("Oops!!! You Lose...")
        print(f"{Choices[user]} vs {Choices[AI]}")
        print("Paper Wins!")

    elif(AI == 0 and user == 1):
        print("Congratulations! You Won...")
        print(f"{Choices[user]} vs {Choices[AI]}")
        print("Rock Wins!")

    elif(AI == 0 and user == -1):
        print("Oops!!! You Lose...")
        print(f"{Choices[user]} vs {Choices[AI]}")
        print("Scissor Wins!")

    else:
        print("Something went wrong!")