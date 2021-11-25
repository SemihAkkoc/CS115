"""
This program that inputs an integer number
from the user and prints the factors of that number
"""

# getting input from user
num = int(float(input('Enter an int: ')))

if num != 0:
    print(f'Factor of {num}:')

# checking whether number is 0 or not
if num > 0:
    for i in range(num):
        # if num is divisible then printing
        if num % (i + 1) == 0:
            if (i + 1) != num:
                print(f'{i + 1},', end='')
            # for last number printing without comma
            else:
                print(f'{i + 1}')

# if number is negative entering this if statement
elif num < 0:
    for i in range(abs(num), 0, -1):

        if abs(num) % i == 0:
            print(f'-{i},', end='')

    for i in range(abs(num)):
        if abs(num) % (i + 1) == 0:
            # if num is divisible then printing
            if (i + 1) != abs(num):
                print(f'{i + 1},', end='')

            # for last number printing without comma
            else:
                print(f'{i + 1}')

else:
    # if 0 entered printing this
    print('Number 0 has no factor.')
