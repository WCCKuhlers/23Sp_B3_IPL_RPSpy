# Khachikyan Rock, paper, Scissors


import math
from random import randint
import random
#rock = 1
#paper = 2
#scissors = 3

playerAns = str(input("Pick rock, paper or scissors: ")) #string = text 
comAns = random.randint(1,3)

start_game = True
score = 0
if comAns == 1:
    comAns = "rock"
if comAns == 2:
    comAns = "paper"
if comAns == 3:
    comAns = "scissors"
                   
while playerAns == comAns:
    print("It is a tie! Pick again!")
    start_game = True
if playerAns == "rock" and comAns == "scissors":
    print("Your rock won the scissors!  Do you want to play again?")
    if playerAns == "yes":
        start_game = True
    else:
        start_game = False
    score = score + 1
if playerAns == "rock" and comAns == "paper":
    print("Your rock lost to the paper. Game over. Do you want to play again?")
    if playerAns == "yes":
        start_game = True
    else:
        start_game = False
if playerAns == "paper" and comAns == "rock":
    print("Your paper won the rock! Do you want to play again?")
    if playerAns == "yes":
        start_game = True
    else:
        start_game = False
    score = score + 1
if playerAns == "paper" and comAns == "scissors":
    print("Your paper lost to the scissors. Game over. Do you want to play again?")
    if playerAns == "yes":
        start_game = True
    else:
        start_game = False
if playerAns == "scissors" and comAns == "rock":
    print("Your scissors lost to the rock. Game over. Do you want to play again?")
    if playerAns == "yes":
        start_game = True
    else:
        start_game = False
if playerAns == "scissors" and comAns == "paper":
    print ("Your scissors won the paper! Do you want to play again?")
    if playerAns == "yes":
        start_game = True
    else:
        start_game = False
    score = score + 1
