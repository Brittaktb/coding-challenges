'''
Poker Dice Game

The aim of this challenge is to create a simplified game
of Poker Dice using only three dice. The computer will generate
three random numbers between 1 and 6.
The program will then check to see if the three dice have
the same value (“Three of a kind!”) or if any two of the three
dice have the same value (“Pair”).
'''

import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)

print(f"Dice-1:" + str(die1))
print(f"Dice-2:{die2}")
print(f"Dice-3:{die3}")

if die1 == die2 and die2 == die3:
    print("Three of a kind!!!")
elif die1 == die2 or die2 == die3 or die1 == die3:
    print("1 Pair!!!")
else:
    print("Better luck next time!")


    
    