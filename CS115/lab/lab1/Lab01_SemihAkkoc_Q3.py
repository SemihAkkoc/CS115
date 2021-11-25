"""
This program asks user to input three names: displays the longest name
"""

# getting inputs from the user
first_name = input('Enter first name: ')
second_name = input('Enter second name: ')
third_name = input('Enter third name: ')

# comparing names and displaying the output
if len(first_name) >= len(second_name) and len(first_name) >= len(third_name):
    if len(first_name) == len(second_name) or len(first_name) == len(third_name):
        print(first_name, '\'s name is the longest, but there is a tie!')
    else:
        print(first_name, '\'s name is the longest')


elif len(second_name) >= len(third_name) and len(second_name) >= len(first_name):
    if len(second_name) == len(third_name) or len(second_name) == len(first_name):
        print(second_name, '\'s name is the longest, but there is a tie!')
    else:
        print(second_name, '\'s name is the longest')


elif len(third_name) >= len(first_name) and len(third_name) >= len(second_name):
    if len(third_name) == len(first_name) or len(third_name) == len(second_name):
        print(third_name, '\'s name is the longest, but there is a tie!')
    else:
        print(third_name, '\'s name is the longest')
