import random
from time import sleep

choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)

player = False

while player == False:
    print("welcome to rock, paper and scissors!")
    print("\nPlease, wait the game is loading...")
    sleep(3)
    player = input("which one do you want to choose?\n'rock': 'rock'\n'paper': 'paper'\n'scissors': 'scissors'\n'stop the game': 'stop':")
    if player == computer:
        print("\nplease wait we are loading your results....")
        sleep(2)
        print("it's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("\nplease wait we are loading your results....")
            sleep(2)
            print("you have lost!!")
        else:
            print("\nplease wait we are loading your results....")
            sleep(2)
            print("you have won!!")
    elif player == "scissors":
        if computer == "rock":
            print("\nplease wait we are loading your results....")
            sleep(2)
            print("you have lost!!")
        else:
            print("\nplease wait we are loading your results....")
            sleep(2)
            print("you have won!!")
    elif player == "paper":
        if computer == "scissors":
            print("\nplease wait we are loading your results....")
            sleep(2)
            print("you have lost!!")
        else:
            print("\nplease wait we are loading your results....")
            sleep(2)
            print("you have won!!")
    elif player == "stop":
        print("thanks for playing!!")
        break
    else:
        print("that's not a valid play!!")
        break

    player = False
# By: Tejaswi Reddy
