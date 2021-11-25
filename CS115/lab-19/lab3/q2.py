# this programme determines which numbers are prime in given interval

def is_prime(n):
    """
    This method returns a bool expression after determining the given n
    is prime or not
    :param n: given integer
    :return: bool: True or False
    """
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def list_primes(a, b):
    """
    This method gives the list of prime numbers in interval [a,b]
    :param a: first integer
    :param b: second integer
    :return: list_of_primes: list of primes in interval [a,b]
    """
    if a < b:
        list_of_primes = []
        for i in range(a, b+1):
            if is_prime(i):
                list_of_primes.append(i)
        return list_of_primes
    else:
        print(f'1<{a}<{b} is NOT satisfied')


for i in list_primes(int(input('Enter a positive integer a: ')), int(input('Enter another positive integer b: '))):
    print(i, 'is a prime')
