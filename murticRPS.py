# murtic Rock, Paper, Sissors

import math
from random import randint
import random

#rock = 1
#paper = 2
#sissors = 3


attempts = 1

while True:
    playerAns = str(input("Pick rock, paper, or sissors "))
    comAns = random.randint(1,3)

    if comAns == 1: #condition
        comAns = "rock" #TRUE
    if comAns == 2: #condition
        comAns = "paper" #TRUE
    if comAns == 3: #condition
        comAns = "scissors" #TRUE

    if comAns == playerAns:
        print("It's a tie")
        attempts = attempts + 1
    if comAns == "rock" and playerAns == "paper":   
        print("Player ", playerAns, "covers computer ", comAns, ",player wins")
        break
        attempts = attempts + 1
    if comAns == "paper" and playerAns == "rock":
        print("Player", playerAns,"got covered by", comAns, ",computer won")
        attempts = attempts + 1
    if comAns == "scissors" and playerAns == "paper":
        print("Computer", comAns, "cut players", playerAns, ",computer won")
        attempts = attempts + 1
    if comAns == "paper" and playerAns == "scissors":
        print("Players", playerAns, "cuts computers", comAns, ",player won")
        break
    if comAns == "rock" and playerAns == "scissors":
        print("Computers", comAns, "smashed players", playerAns, ",computer won")
        attempts = attempts + 1
    if comAns == "scissors" and playerAns == "rock":
        print("Players", playerAns, "smashed computers", comAns, ",player won")
        break
print("You Won. It took you " ,attempts, " attempts to beat the computer")


        
#if comAns == playerAns:
    #print("It's a tie")
#elif comAns ("rock") == playerAns ("paper"):
   # print("You beat the computer!")
