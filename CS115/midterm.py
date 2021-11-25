def distance(filename, origin, destination):
    file = open(filename, 'r')  # do not forget to close
    for line in file:
        curr_line = line.split(',')
        curr_line[-1].strip()
        if curr_line[0].lower() == origin.lower():
            if curr_line[1].lower() == destination.lower():
                return curr_line[2]
    file.close()
    return -1


def is_spaced(password):
    for i in range(2, len(password)):
        if int(password[i-2])-int(password[i-1]) != int(password[i-1]) - int(password[i]):
            return True
    return False


def contain_birthday(password, b_day):
    b_day = str(b_day)
    for i in password:
        for j in range(len(b_day)):
            if b_day[j] == i:
                pass


def hailstone(n):
    print(n, end=' ')
    if n == 1:
        return None
    elif n % 2 == 0:
        hailstone(n//2)
    else:
        hailstone(3*n+1)


def import_cars(filename, cars_dict):
    file = open(filename, 'r')
    for line in file:
        car = line.split(':')
        car[-1] = car[-1].rstrip()
        if car[0] in cars_dict:
            cars_dict[car[0]] += (car[1], )
        else:
            cars_dict[car[0]] = (car[1], )


def find_by_city(code, cars_dict):
    brand_list = []
    total_cars, in_city = 0, 0
    for brand in cars_dict:
        for car in cars_dict[brand]:
            total_cars += 1
            if car[:2] == code and not (brand in brand_list):
                brand_list.append(brand)
            if car[:2] == code:
                in_city += 1
    per = (in_city / total_cars) * 100
    return brand_list, per

'''
cars = {}
import_cars('cars.txt', cars)
city_code = input('Enter city code to search: ')
models, percentage = find_by_city(city_code, cars)
print('Models with city code', city_code, models)
print('Percentage of cars from', city_code, ':', percentage)
'''


def DecimalToBinary(num):
    if num >= 1:
       DecimalToBinary(num // 2)
       print(str(num % 2), end='')


DecimalToBinary(4444444444)
"""
n = int(input())
for i in range(n):
    if (n-i) % 2 == 0:
        print(' ' * ((n-i)//2) + '*' * (i+1))
"""