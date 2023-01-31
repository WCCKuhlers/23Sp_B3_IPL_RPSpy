#RockPaperScissors

import math
from random import randint
import random
start_game = True

while start_game:
    rock = 1
    paper = 2
    scissors = 3

    playerAns = str(input("Pick rock, paper, or scrissors "))
    comAns = random.randint(1,3)

    if comAns == 1: #condition
        comAns = "rock" #TRUIE
    if comAns == 2: #condition
        comAns = "paper" #TRUE
    if comAns == 3: #condition
        comAns = "scissors" #TRUE

    if comAns == playerAns:
        print("Tie")
    if comAns == "rock" and playerAns == "paper":
        #print("Player Wins")
        print("Player", playerAns, "covers computer ", comAns, ": player wins")
    if comAns == "rock" and playerAns == "scissors":
        #print("Computer Wins")
        print("Computer", comAns, "crushes player", playerAns, ": computer wins")
    if comAns == "paper" and playerAns == "rock":
        #print("Computer Wins")
        print("Computer", comAns, "covers player", playerAns, ": computer wins")
    if comAns == "paper" and playerAns == "scissors":
        #print("Player Wins")
        print("Player", playerAns, "cuts computer", comAns, ": player wins")
    if comAns == "scissors" and playerAns == "rock":
        #print("Player Wins")
        print("Player", playerAns, "crushes computer", comAns, ": player wins")
    if comAns == "scissors" and playerAns == "paper":
       #print("Computer Wins")
        print("Computer", comAns, "cuts player", playerAns, ": computer wins:")

    playerResp = str(input("Would you like to play again? yes or no "))

    if playerResp == "yes":
        start_game = True
    else:
        start_game = False
    


