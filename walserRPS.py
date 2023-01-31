# Rock, Paper, Scissors


import math
from random import randint
import random


rock = 1
paper = 2
scissors = 3

playAns = str(input("Pick rock, paper, or scissors "))
comAns = random.randint(1,3)

if comAns == 1: # condition
    comAns = "rock" # TRUE
if comAns == 2:
    comAns = "paper"
if comAns == 3:
    comAns = "scissors"

if comAns == playAns:
    print("It's a tie")
if comAns == "rock" and playAns == "paper":
    print("Your ", playAns, "covers computer's", comAns, " -  You win")
if comAns == "rock" and playAns == "scissors":
    print("Your ", playAns, "was crushed by computer's", comAns, " -  You lose")
if comAns == "scissors" and playAns == "paper":
    print("Your ", playAns, "was cut by computer's", comAns, " -  You lose")
if comAns == "scissors" and playAns == "rock":
    print("Your ", playAns, "smashes computer's", comAns, " -  You win")
if comAns == "paper" and playAns == "rock":
    print("Your ", playAns, "is covered by computer's", comAns, " -  You lose")
if comAns == "paper" and playAns == "scissors":
    print("Your ", playAns, "cut computer's", comAns, " -  You win")




#if playAns == comAns:
#    print("It's a tie.")
#else:
#    if playAns == 1:
#        if comAns == 2:
#            print("Computer chose paper - Computer wins")
#        else:
#            print("Computer chose scissors - you win")
#    else:
#        if playAns == 2:
#            if comAns == 1:
#                print("Computer chose rock - you win")
#            else:
#                print("Computer chose scissors - Computer wins")
#        else:
#            if comAns == 1:
#                print("Computer chose rock - Computer wins")
#            else:
#                print("Computer chose paper - you win")
                

