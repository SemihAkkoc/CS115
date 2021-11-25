"""
This program prompts the user to enter a string until
an empty string is entered. For each input string, it
displays a new string created by collecting even position
letters followed by odd position letters from the input string.
"""

# getting string input from user
text = input('Enter a string: ')

while len(text) > 0:

    # defining empty strings
    even_string = ''
    odd_string = ''

    # in for loop creating even and odd strings
    for i in range(len(text)):
        if i % 2 == 0:
            even_string += text[i]

        else:
            odd_string += text[i]

    # printing even and odd string
    print(f'new string is {even_string}{odd_string}\n')

    # getting new input
    text = input('Enter a string: ')

# goodbye my friend
print('done!')

