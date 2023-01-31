#tomkinsRPS

import math
from random import randint
import random

# rock = 1
# paper = 2
# scissors = 3

playerAns = str(input("Pick rock, paper, scissors "))
comAns = random.randint(1,3)

if comAns == 1: # condition
    comAns = "rock" # TRUE
if comAns == 2: # condition
    comAns = "paper" # TRUE
if comAns == 3: # condition
    comAns = "scissors" # TRUE
if comAns == playerAns:
    print("Tie")
if comAns == "rock" and playerAns == "paper":
    print("Player ", playerAns, "covers ", comAns, "Player wins")
if comAns == "paper" and playerAns == "scissors":
    print("Player ", playerAns, "cuts computer ", comAns, "Player wins")
if comAns == "scissors" and playerAns == "rock":
    print("Player ", playerAns, "smashes ", comAns, "Player wins")
if comAns == "rock" and playerAns == "scissors":
    print("Computer ", comAns, "smashes ", playerAns, "Computer wins")
if comAns == "paper" and playerAns == "rock":
    print("Computer ", comAns, "covers ", playerAns, "Computer wins")
if comAns == "scissors" and playerAns == "paper":
    print("Computer ", comAns, "cuts player ", playerAns, "Computer wins")
 
