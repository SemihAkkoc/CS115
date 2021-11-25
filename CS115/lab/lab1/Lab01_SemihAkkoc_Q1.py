"""
This program gets 3 real numbers from user and calculates the result of a given equation

Equation is:
f(x,y,z) = (x+y*z)*(x*y+z)/x*y*z
"""

# getting float type inputs from user
x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

# calculation the result and
# printing the results according to the given equation
# checks
if x == 0 or y == 0 or z == 0:
    print('Do not enter 0')

else:
    result = (x + y * z) * (x * y + z) / (x * y * z)
    print(f'f({x:.1f},{y:.1f},{z:.1f}) = {result:.2f}')
