# first exercise
# this function tell if the input number is divisible by 5 or 7
def num_5_7_divisible():
    num = int(input('Please enter an integer: '))
    if num%5==0 and num%7!=0:
        print(f'{num} is divisible by 5.')
    elif num%7==0 and num%5!=0:
        print(f'{num} is divisible by 7.')
    elif num%5==0 and num%7==0:
        print(f'{num} is divisible by 5 and 7.')
    else:
        print(f'{num} is not divisible by 5 or 7.')

num_5_7_divisible()

# second exercise
# this function is a guessing game
import random
def guess_game():
    result = False
    num=int(random.uniform(1,9))
    for i in range(3):
        users_guess = int(input('Guess the lucky number: '))
        if num == users_guess:
            print(f'Correct guess. You guessed it in {i+1}.')
            result=True
            break
        else:
            print(f'Wrong guess. You have {2-i} chances to guess left.')
    if not result:
        print(f'You guessed it wrong. Correct answer was {num}.')

guess_game()

# third exercise
# this function determines if the given word has same letter in beginning and in the end
def word_beginning_end():
    word = input('Please enter a word: ')
    if word[0]==word[-1]:
        print(f'{word} has same letter in the beginning end in the end.')
    else:
        print(f'{word} is useless.')

word_beginning_end()

# fourth exercise
# this function gives bmi and tells what type of body you have
def bmi_calculator():
    weight=float(input('Please enter your weight in kilograms: '))
    height=float(input('Please enter your height in meters: '))
    bmi = weight/height**2
    print(f'Your body mass index is: {bmi:.2f}')
    if bmi >= 30:
        print('Obese')
    elif 25 <= bmi < 30:
        print('Overweight')
    elif 20 <= bmi < 25:
        print('Normal')
    elif bmi < 20:
        print('Underweight')

bmi_calculator()