# Dice Rolling Simulator

# The Goal: Like the title suggests, this project involves writing a program that simulates
# rolling dice. When the program runs,  it will randomly choose a number between 1 and 6.
# (Or whatever other integer you prefer — the number of sides on the die is up to you.)
# The program will print what that number is. It should then ask you if you’d like to roll
# again. For this project, you’ll need  to set the min and max number that your dice can produce.
# For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function
# that randomly grabs a number within that range and prints it.

# use the specifications of the RANDOM library
import random

# Flag to set initial use
_flag = 1


# function to generate random faces


def numbergenerator(_faces):
    """ Returns a random positive integer with range between 1 and the entered value"""
    _randomNumber = random.randint(1, _faces)
    return _randomNumber


# validate reuse
while _flag >= 0:
    # Set up the dice model
    _faces = int(input(r"Enter a number from 1 to 10 to specify your dice"));
    # print the generated number
    _generatedNumber = numbergenerator(_faces)
    print("Dice side drawn : ", _generatedNumber);
    # user input
    _retry = input("Type Q to quit else retry luck !!!").upper()
    print(_retry)
    if _retry == 'Q':
        # Setting flag less than 1 quits the while loop
        _flag = -1
        print("Thanks for playing !!!")
