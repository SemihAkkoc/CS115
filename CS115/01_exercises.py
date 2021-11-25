# first exercise
# this function converts kelvin value to celsius value
def convert_kelvin_to_celsius(kelvin_value):
    degree_sign = u"\N{DEGREE SIGN}"
    celsius_value = kelvin_value - 273
    print(f'{kelvin_value:.1f}K is equal to {celsius_value:.1f}{degree_sign}C in Celsius.')

convert_kelvin_to_celsius(400)

# second exercise
# this function calculates the area of a circle with given radius
import math

def calculate_area_of_circle(radius):
    area = math.pi * (radius ** 2)
    print(f'With given radius of {radius:.2f}cm the area of this circle is {area:.2f}cm\u00b2.')

calculate_area_of_circle(1.5)

# third exercise
# this function writes the first and last digit of some 4-digit number
import random

def first_last_digit(four_digit_number):
    first_digit = four_digit_number//1000
    last_digit = four_digit_number%10
    print(f'This {four_digit_number} numbers first digit is {first_digit}, last digit is {last_digit}.')

first_last_digit(int(random.uniform(1000,9999)))

# forth exercise
# this function gives the number of hours and minutes needed for a car to travel given distance at given velocity

def calculate_time(distance, velocity):
    time = distance/velocity*60  #v=x/t
    print(f'A car would travel {distance}km at the velocity {velocity}km/h in {int(time//60)} hours and {time%60:.1f} minutes.')

calculate_time(500,110)


class new:
    def __init__(self, n, y):
        self.__name = n
        self.__year = y
