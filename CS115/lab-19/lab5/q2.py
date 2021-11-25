def add_car(car, license_plate, owner):
    if license_plate in car:
        print('car has already registered.')
    else:
        car[license_plate] = list(owner)
        print('Done')


def update_car(car, license_plate, owner):
    if not (license_plate in car):
        print('this car does not exist')
    else:
        car[license_plate] = car[license_plate].append(owner)


def find_car(car, license_plate):
    if license_plate in car:
        return car[license_plate]


cars = {}
while True:
    print('1)Add \n'
          '2)Search Car \n'
          '3)Update Owner\n'
          '4)Quit =>', end=' ')

    match int(input()):
        case 1:
            add_car(cars, input('Enter license plate:'), input('Enter owner name: '))
        case 2:
            update_car(cars, input('Enter license plate:'), input('Enter owner name: '))
        case 3:
            find_car(cars, input('Enter license plate:'))
        case 4:
            break
        case _:
            print('Unknown menu')

