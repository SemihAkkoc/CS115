"""
This program prompts the user for a desired sum until 0 is entered.
For each desired sum input value, it repeatedly rolls two six-sided dice
until their sum is the desired sum and reports
the number of rolls to achieve the desired sum.
"""

# from random module we are importing randint function
from random import randint

# getting input from user
wanted_sum = int(float(input('Desired dice sum: ')))

# defining variables
count = 0
loop_on = True

# entering loop and in loop checking whether conditions are satisfied
while loop_on:
    # creating dices
    first_dice = randint(1, 6)
    second_dice = randint(1, 6)
    count += 1

    # if 0 entered exiting loop
    if wanted_sum == 0:
        loop_on = False

    # checking if wanted_sum in desired range and if not printing invalid
    elif wanted_sum > 12 or wanted_sum < 2:
        print('Invalid dice sum, try again...\n')
        wanted_sum = int(float(input('Desired dice sum: ')))

    # if wanted_sum is equal to sum of dices print count
    elif first_dice + second_dice == wanted_sum:
        print(f'{count} rolls\n')
        wanted_sum = int(float(input('Desired dice sum: ')))
        count = 0


# saying goodbye i'll miss you
print('bye!')


def my_upper(string):
    """
    takes a string s as a parameter and returns True
    if the input string s is neat reversible, False otherwise

    Parameters:
           string (str): A string
    Returns:
           (str): returns upper cased string
    """

    upper_string = ''

    for i in string:
        if ord(i) > 96:
            upper_string += chr(ord(i)-32)
        else:
            upper_string += i

    return upper_string
