"""
This program takes inputs three integers from the user
and reports the largest even input and the sum of even inputs.
"""

# defining variables
sum_even = 0
biggest_num = 0

is_first_even = False
is_second_even = False
is_third_even = False

# getting input from the user
first_integer = int(input('Enter first integer: '))
second_integer = int(input('Enter second integer: '))
third_integer = int(input('Enter third integer: '))

# checking whether the numbers are even
if first_integer % 2 == 0:
    sum_even += first_integer
    is_first_even = True

if second_integer % 2 == 0:
    sum_even += second_integer
    is_second_even = True

if third_integer % 2 == 0:
    sum_even += third_integer
    is_third_even = True

# if all numbers are even
if is_first_even and is_second_even and is_third_even:
    if first_integer > second_integer and first_integer > third_integer:
        biggest_num = first_integer
    elif second_integer > first_integer and second_integer > third_integer:
        biggest_num = second_integer
    else:
        biggest_num = third_integer

# if one of the number is not even
if not is_first_even and is_second_even and is_third_even:
    if second_integer > third_integer:
        biggest_num = second_integer

    else:
        biggest_num = third_integer


if is_first_even and not is_second_even and is_third_even:
    if first_integer > third_integer:
        biggest_num = first_integer

    else:
        biggest_num = third_integer


if is_first_even and is_second_even and not is_third_even:
    if second_integer > first_integer:
        biggest_num = second_integer

    else:
        biggest_num = first_integer

# if two of the numbers are not even
if not is_first_even and not is_second_even and is_third_even:
    biggest_num = third_integer

if not is_first_even and is_second_even and not is_third_even:
    biggest_num = second_integer

if is_first_even and not is_second_even and not is_third_even:
    biggest_num = first_integer

# printing the results
if not is_first_even and not is_second_even and not is_third_even:
    print('No even integer is entered')
else:
    print(f'sum of evens is {sum_even}')
    print(f'even max is {biggest_num}')