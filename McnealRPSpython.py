    #Rock, Paper, Scissors

import math
from random import randint
import random

#rock = 1
#paper = 2
#scissors = 3

playerAns = str(input("Pick rock, paper, or scissors"))

comAns = random.randint(1,3)

if comAns == 1:
    comAns = "rock"
if comAns == 2:
    comAns = "paper"
if comAns == 3:
    comAns = "scissors"

if comAns == playerAns:
        print("Tie")
if comAns == "rock" and playerAns == "paper":
    #print("player wins!")
    print("computers rock is covered by players paper. player wins!")
if comAns == "paper" and playerAns == "scissors":
    #print("player wins!")
    print("computers paper is cut by players scissors. player wins!")
if comAns == "scissors" and playerAns == "rock":
    #print("player wins!")
    print("computers scissors are broken by players rock. player wins!")
if comAns == "rock" and playerAns == "scissors":
    #print("computer wins!")
    print("computers rock breaks players scissors. computer wins!")
if comAns == "paper" and playerAns == "rock":
    #print("computer wins!")
    print("computers paper covers players rock. computer wins!")
if comAns == "scissors" and playerAns == "paper":
    #print("computer wins!")
    print("computers scissors cuts players paper. computer wins!")
#print("player ", playerAns, "covers computer", comAns, "Player win!")

