import math
from random import randint
import random
win=0
##rock=1
##paper=2
##scissors=3
start=True
score=0
while start:
    playerAns=str(input("Rock, Paper, or Scissors "))
    comAns=random.randint(1,3)

    if comAns == 1: #condition
        comAns="Rock" #true
    if comAns == 2: #condition
        comAns="Paper" #true
    if comAns == 3: #condition
        comAns="Scissors" #true

    if comAns == playerAns:
        print("Tie")
    if comAns=="Rock" and playerAns =="Paper":
        win=1
        #print("Player",playerAns "covers computer",comAns". Player wins!")
    if comAns=="Rock" and playerAns == "Scissors":
        win=2
    if comAns=="Paper" and playerAns == "Rock":
        win=2
    if comAns=="Scissors" and playerAns == "Paper":
        win=2
    if comAns=="Scissors" and playerAns == "Rock":
        win=1
    if comAns=="Paper" and playerAns == "Scissors":
        win=1
    if win==1:
        print (playerAns, "beats", comAns)
        print("Player wins!")
        score=score+1
    if win==2:
        print (comAns, "beats", playerAns)
        print("Computer wins!")
    print("Score is:",score)
    print("----------")
