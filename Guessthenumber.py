# Guess the Number

# The Goal: Similar to the first project, this project also uses the random module in Python.
# The program will first randomly generate a number unknown to the user. The user needs to
# guess what that number is. (In other words, the user needs to be able to input information.)
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong
# (e.g. The number is too high or too low). If the user guesses correctly, a positive indication
# should appear. You’ll need functions to check if the user input is an actual number, to see the
# difference between the inputted number and the randomly generated numbers, and to then compare
# the numbers.

from RollingDice import numbergenerator


# Set the session start value with a positive integer
_flag = 1
# Set the maximum value of the predicted number
_range = 999
# Generate a random number
_generatedNumber = numbergenerator(_range)
_unmatchedGuess = 1
# Guess the number

while _flag == 1:
    _guessedNumber = int(input("Enter your guess"))
            if abs(_guessedNumber - _generatedNumber) > 15:
                print("Number is too big!!, Guess again. ")
            elif abs(_guessedNumber - _generatedNumber) > 5:
                print("Number is big!!, Guess again. ")
            elif abs(_guessedNumber - _generatedNumber) > 1:
                print("Close guess !!")
            else:
                print("Accurate Guess.")
    exit


