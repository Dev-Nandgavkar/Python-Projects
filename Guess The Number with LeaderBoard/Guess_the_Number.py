# Guess The Number Game
# A Random Number will be Generated and you have to guess the number.

import random

def playzone():

    random_Num = random.randint(1,100)
    user_num = -1
    guess_no = 1
    while(user_num != random_Num):
        user_num = int(input("\nGuess The Number: "))
        if(user_num > random_Num):
            print("Lower Number")
            guess_no += 1
        elif(user_num < random_Num):
            print("Higher Number")
            guess_no += 1

    print("\nCongratulations!!! You Have Guessed the Number")
    print(f"Number = {random_Num}")
    print(f"Guessed Attempts: {guess_no}\n")

    Update_score(guess_no)
    print(f"Highest Score: {check_score()}")
    print(f"Your Score: {guess_no}\n")

    play_again()

    

def check_score():
    with open("Mini Projects\\High_Score.txt") as f:
        high_score = f.read()
        if(high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0
    return high_score
    

def Update_score(guess_no):
    
    score = guess_no

    with open("Mini Projects\\High_Score.txt") as f:
        high_score = f.read()
        if(high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0

    if(score<high_score):
        with open("Mini Projects\\High_Score.txt", "w") as f:
            f.write(str(score))
    return score

def play_again():
    while True:
        play = input("\nPress Y to Try Again\nPress N to Exit: \n").upper()
        if play == "Y":
            start_game()
            return True
        elif play == "N":
            exit()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def start_game():
    print("\nWelcome to Guess The Number Game\n")
    print(f"Current High Score: {check_score()}")
    print()

    print("Press \"1\" to Play")
    print("Press \"0\" to Exit")
    play_input = int(input("Enter Your Choice: "))

    if(play_input == 1):
        playzone()
    else:
        exit()

start_game()
    
