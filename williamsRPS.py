# Name file williamsRPS for Rock, Paper, and Scissors
import math
import random

#rock = 1
#paper = 2
#scissors = 3

#breaks out of loop when you win

attempts = 0

while True:
    playerAns = str(input("Pick rock, paper or scissors: "))
    cmpAns = random.randint(1,3)


    if cmpAns == 1:
        cmpAns = "rock"
    elif cmpAns == 2:
        cmpAns = "paper"
    elif cmpAns == 3:
        cmpAns = "scissors"
        
    
    if playerAns == cmpAns:
        print(f"computer chose {cmpAns}")
        print("Tie!")
        attempts += 1
        
    elif playerAns == "paper" and cmpAns == "rock":
        print(f"computer chose {cmpAns}")
        print("you beat the computer")
        print()
        break
        
    elif playerAns == "scissors" and cmpAns == "paper":
        print(f"computer chose {cmpAns}")
        print("you beat the computer")
        print()
        break
        
    elif playerAns == "rock" and cmpAns == "scissors":
        print(f"computer chose {cmpAns}")
        print("you beat the computer")
        print()
        break
        
    elif playerAns == "rock" or playerAns == "paper" or playerAns == "scissors":
        print(f"computer chose {cmpAns}")
        print("you lost to the computer")
        print()
        attempts += 1
    else:
        print("Please enter rock, paper, or scissors")
        exit()
print(f"You won, it took you {attempts} attempts to win!")
  

