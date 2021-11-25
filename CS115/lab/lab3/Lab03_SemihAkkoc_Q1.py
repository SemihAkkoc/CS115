"""
This program contains some functions
"""


def my_upper(string):
    """
    this function return the upper case version of given string

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


def my_find(s, char, index=0):
    """
    this function return the index of desired character

    Parameters:
           s (str): A string
           char (str): a character
           index (int): from which index
    Returns:
           (int): returns index of desired character
    """
    for i in range(index, len(s)):
        if s[i] == char:
            return i
    return -1


def is_neat_reversible(s):
    """
    takes a string s as a parameter and returns True
    if the input string s is neat reversible, False otherwise

    Parameters:
           s (str): A string
    Returns:
           bool: returns bool accordingly if given string satisfies condition
    """
    if not s:
        return False

    temp_s = s[1::] + s[0]  # creating new string but not reversed

    if temp_s[::-1] == s:  # checking whether reversed string satisfies the condition
        return True

    return False


def uppercase_word_at(s, index):
    """
    takes a string s and an integer index as parameters and returns a string which is
    identical to s except the letters in s starting from the specified index up to the
    first space character are capitalized.

    Parameters:
           s (str): a string
           index (int): index number
    Returns:
           new_string (str): returns the desired string
    """

    new_string = ''
    stop_index = my_find(s, ' ', index)
    if stop_index == -1:
        stop_index = len(s)

    for i in range(len(s)):
        if index <= i <= stop_index:

            new_string += my_upper(s[i])
        else:
            new_string += s[i]

    return new_string


def capitalize_neat_reversible(s):
    """
    takes a string s as a parameter,and using the functions created before it
    creates and returns a new string in which all neat reversible words are capitalized

    Parameters:
           s (str): a string
    Returns:
           str: returns the desired string
    """
    s += ' '
    new_string = ''
    curr_space_index = my_find(s, ' ')
    last_space_index = 0
    s = 'hello world and hi'
    while curr_space_index != -1:
        if is_neat_reversible(s[last_space_index:curr_space_index]):
            new_string += uppercase_word_at(s[last_space_index:curr_space_index], -1) + ' '
        else:
            new_string += s[last_space_index:curr_space_index] + ' '

        last_space_index = curr_space_index + 1
        curr_space_index = my_find(s, ' ', last_space_index)

    return new_string


# getting input from user
s = input('Enter a sentence: ')

while s:  # looping until empty string is entered
    print('neat reversible capitalized: ', end='\n ')
    print(capitalize_neat_reversible(s))
    s = input('\nEnter a sentence: ')

print('bye!')  # goodbye my friend this was hard
