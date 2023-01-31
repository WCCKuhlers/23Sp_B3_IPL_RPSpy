import math
from  random import randint
import random

print("Are you ready to play?")
start_game = False
if "yes": start_game = True
if "no": start_game = False

# rock = 1
# paper = 2
# scissors = 3

playerAns = str(input("Pick rock, paper, or scissors "))
comAns = random.randint(1,3)

if comAns == 1: #condition
    comAns = "rock" #TRUE
if comAns == 2: #condition
    comAns = "paper" #TRUE
if comAns == 3: #condition
    comAns = "scissors" #TRUE


if comAns == playerAns:
    print("Tie")
if comAns == "rock" and playerAns == "paper":
    print("Player", playerAns, "covers", comAns, ": Player wins")
if comAns == "rock" and playerAns == "scissors":
    print(comAns, "crushes", playerAns, ": Computer won")
if comAns == "paper" and playerAns == "rock":
    print(comAns, "covers", playerAns, ": Computer won")
if comAns == "paper" and playerAns == "scissors":
    print(comAns, "cuts", playerAns, ": Player won")
if comAns == "scissors" and playerAns == "rock":
    print(comAns, "crushes", playerAns, ": Player won")
if comAns == "scissors" and playerAns == "paper":
    print(comAns, "cuts", playerAns, ": Computer won")



























