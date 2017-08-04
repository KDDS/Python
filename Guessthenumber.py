# Guess the Number

# The Goal: Similar to the first project, this project also uses the random module in Python.
# The program will first randomly generate a number unknown to the user. The user needs to
# guess what that number is. (In other words, the user needs to be able to input information.)
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong
# (e.g. The number is too high or too low). If the user guesses correctly, a positive indication
# should appear. You’ll need functions to check if the user input is an actual number, to see the
# difference between the inputted number and the randomly generated numbers, and to then compare
# the numbers.
import random


# function to generate random faces


def numbergenerator(_faces):
    """ Returns a random positive integer with range between 1 and the entered value"""
    _randomNumber = random.randint(1, _faces)
    return _randomNumber

# Setting the session values
_flag = 1
_retries = 1
_max_retry = 4
_score = 0
# Set the maximum value of the predicted number
_range = 15
# Generate a random number
_generatedNumber = numbergenerator(_range)
print ("You have {0} chances for an accurate guess !".format(_max_retry))
# Guess the number

while _flag > 0 or _retries <= _max_retry:
    _guessedNumber = int(input("Luck pot:[{0}]. Enter your guess :- ".format(_max_retry - _retries+1)))
    if abs(_guessedNumber - _generatedNumber) > 10:
        print("Guess is wayyy bigger. ")
        _score = _score + 10
    elif abs(_guessedNumber - _generatedNumber) > 8:
        print("Guess is big!!, try again. ")
        _score = _score + 25
    elif abs(_guessedNumber - _generatedNumber) > 5:
        print("Close guess. ")
        _score = _score + 50
    elif abs(_guessedNumber - _generatedNumber) >= 1:
        print("Almost there!!! ")
        _score = _score + 80
    else:
        print("Bull's eye. number {0} correctly guessed".format(_generatedNumber))
        _score = _score + 100
        _flag = -1

    _retries = _retries + 1
    
    if _retries > _max_retry:
        print("You ran out of luck. Poor you, the number was {0}".format(_generatedNumber))
        _flag = -1

    # user input
    if _flag == -1:
        print("Your score is {0} ".format(_score))
        _retry = input("Type Q to quit else retry luck !!!").upper()
        if _retry == 'Q':
            # Setting flag less than 1 quits the while loop
            _flag = -1
            print("Thanks for playing !!!")
        else:
            _flag = 1
            _retries = 0
            _score = 0



