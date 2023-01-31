# Name file VelicRPS for Rock, Paper, Scissors

import math
from random import randint
import random

score = 1
#rock = 1
#paper = 2
#scissors = 3

while True:
    playerAns = str(input("Pick rock, paper, or scissors "))
    comAns = random.randint(1,3)

    if comAns == 1:
        comAns = "rock"
    if comAns == 2:
            comAns = "paper"
    if comAns == 3:
            comAns = "scissors"
    print("Computer picked", comAns)

    if comAns == playerAns:
        print("It's a tie! ")
        score = score+1
    if comAns == "rock" and playerAns == "paper":
        print ("You win! ")
        print ("It took you", score, "tries to beat the computer! ")
        break
    if comAns == "rock" and playerAns == "scissors":
        print ("Computer wins! ")
        score = score+1
    if comAns == "paper" and playerAns == "rock":
        print ("Computer wins! ")
        score = score+1
    if comAns == "paper" and playerAns == "scissors":
        print ("You win! ")
        print ("It took you", score, "tries to beat the computer! ")
        break
    if comAns == "scissors" and playerAns == "paper":
        print ("Computer wins! ")
        score = score+1
    if comAns == "scissors" and playerAns == "rock":
        print ("You win! ")
        print ("It took you", score, "tries to beat the computer! ")
        break




    
    
