'''
Higher or Lower Number Game
For this challenge you will design and write a program
to play against the computer. The computer will display a random number between 1 and 100. The user will have to try to guess this number. For each guess the computer will inform the user if the number to guess is higher or lower than the user guess. The program will end once 
the user guess matches the number to guess.
'''
import random
numberToGuess = random.randint(1,20)

userGuess = -1


while numberToGuess != userGuess:
    
    userGuess = int(input("Enter a number between 0-20 :"))
    
    if numberToGuess > userGuess:
        print("Output(Higher!)")
    elif numberToGuess < userGuess:
        print("Output(Lower!)")
    else:
        print(f"You Win! The hidden number '{numberToGuess}' is found!")

