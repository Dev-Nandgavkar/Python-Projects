# Rock, Paper & Scissor Game:

# Rock -> 1
# Paper -> -1
# Scissor -> 0

import random

User_Dict = {"r" : 1, "p" : -1, "s" : 0}
Choices = {1 : "Rock", -1 : "Paper", 0 : "Scissors"}

def user_input():
    while True:
        User_Choice = input("Enter Your Choice: ").lower()
        if User_Choice in User_Dict:
            return User_Dict[User_Choice]
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")

def game_Logic(AI, user):
    global user_win,ai_win,draw

    if(AI == user):
        print("Draw")
        print(f"{Choices[user]} vs {Choices[AI]}")
        print("No one Wins")
        draw += 1

    else:
        if(AI == 1 and user == -1) or (AI == 0 and user == 1) or (AI == -1 and user == 0):
            print("Congratulations! You Won...")
            print(f"{Choices[user]} vs {Choices[AI]}")
            print("Paper Wins!")
            user_win += 1

        elif(AI == 1 and user == 0) or (AI == -1 and user == 1) or (AI == 0 and user == -1):
            print("Oops!!! You Lose...")
            print(f"{Choices[user]} vs {Choices[AI]}")
            print("Rock Wins!")
            ai_win += 1

        else:
            print("Something went wrong!")
            exit()
    
def play_again():
    while True:
        play = input("\nPress Y to Try Again\nPress N to Exit: \n").upper()
        if play == "Y":
            playzone()
            return True
        elif play == "N":
            exit()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


def playzone():
    global user_win,ai_win,draw
    
    while True:
        user_win = 0
        ai_win = 0
        draw = 0

        print("\nWelcome To Rock, Paper & Scissors!")
        print("Refer the Following to Play:")
        print("r -> Rock\np -> Paper\ns -> Scissors")

        while user_win < 2 and ai_win < 2:
    
            AI = random.choice([-1, 0, 1])

            print(f"\nRound {user_win + ai_win + draw +1}:")
            user = user_input()
            print(f"\nYou Choose: {Choices[user]} \nComputer Choose: {Choices[AI]}")
            print()
            print("Game Result: ")
            game_Logic(AI, user)
            print(f"\nScore:\nYou: {user_win}, Computer: {ai_win}")

        if user_win == 2:
            print("\nCongratulations! You Win the Game!")
            play_again()
        elif ai_win == 2:
            print("\nUnfortunately, You Lose the Game!")
            play_again()

        if play_again():
            playzone()


playzone()

