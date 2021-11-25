#  This programme takes a positive integer n and prints n-n matrix

def matrix_creater(n):
    """
    This method creates n-n matrix

    :param n: positive integer
    :return: None
    """
    from random import randint

    for i in range(n):
        for j in range(n):
            print(randint(0, 1), end=' ')
        print()


matrix_creater(int(input('Enter a positive integer: ')))
