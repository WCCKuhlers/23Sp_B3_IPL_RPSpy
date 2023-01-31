import math
from random import randint
import random

game = True
player_score = 0
computer_score = 0

while game:
    player_ans = str(input("Pick rock, paper, or scissors: "))
    if player_ans == "stop":
        if player_score > computer_score:
            print("player wins")
        else:
            print("computer wins")
        game = False

    com_ans = random.randint(1,3)

    if com_ans == 1:
        com_ans = "rock"
    if com_ans == 2:
        com_ans = "paper"
    if com_ans == 3:
        com_ans = "scissors"
    print("Computer picks:",com_ans)

    if com_ans == player_ans:
        print("tie")
    if com_ans == "scissors" and player_ans == "paper":
        print("computer wins")
        computer_score = computer_score + 1
        print("computer score: ",computer_score)
        print("player score: ",player_score)
    if com_ans == "scissors" and player_ans == "rock":
        print("player wins")
        player_score = player_score + 1
        print("computer score: ",computer_score)
        print("player score: ",player_score)
    if com_ans == "rock" and player_ans == "scissors":
        print("computer wins")
        computer_score = computer_score + 1
        print("computer score: ",computer_score)
        print("player score: ",player_score)
    if com_ans == "rock" and player_ans == "paper":
        print("player wins")
        player_score = player_score + 1
        print("computer score: ",computer_score)
        print("player score: ",player_score)
    if com_ans == "paper" and player_ans == "rock":
        print("computer wins")
        computer_score = computer_score + 1
        print("computer score: ",computer_score)
        print("player score: ",player_score)
    if com_ans == "paper" and player_ans == "scissors":
        print("player wins")
        player_score = player_score + 1
        print("computer score: ",computer_score)
        print("player score: ",player_score)
    

       
