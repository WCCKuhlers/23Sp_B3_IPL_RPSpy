import math
from random import randint
import random
rock = 1
paper = 2
scissors = 3
playerAns = str(input ("pick rock, paper, scissors"))
comAns = random.randint(1,3)

if comAns == 1:
    comAns = "rock"
if comAns == 2:
    conAns = "paper"
if comAns == 3:
    ComAns = "scissors"
    
if comAns == playerAns:
    print ("Tie")
if comAns == "rock" and playerAns == "paper":
    print (playerAns, "covers computer ", comAns, ": Player wins")
if comAns == "rock" and playerAns == "scissors":
    print (comAns, "smashes", playerAns, ": Computer won")
if comAns == "scissors" and playerAns == "paper":
    print (comAns,"shredds", playerAns, ": Computer won")
if comAns == "scissors" and playerAns == "rock":
    print (playerAns, "smashes", comAns, ": Computer won")
if comAns == "paper" and playerAns == "rock":
    print (comAns, "covers computer ", PlayerAns, ": Player wins")   
if comAns == "paper" and playerAns == "scissors":
    print (playerAns,"shredds", comAns, ": Computer won")
