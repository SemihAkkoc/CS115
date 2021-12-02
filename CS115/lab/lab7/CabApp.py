from cab import Hatchback, Sedan

comp_cab = Sedan('Sedan', 10, 2015)


def find_greater(cabs_list, cab):
    greater_cabs = 0
    for current_cab in cabs_list:
        if current_cab > cab:
            greater_cabs += 1
    return greater_cabs


def read_file(filename):
    cabs_list = []
    for line in open(filename, 'r'):
        current_cab = line.split(';')
        current_cab[-1] = current_cab[-1].strip()

        if current_cab[0] == 'Sedan':
            cabs_list.append(Sedan(current_cab[0], current_cab[1], current_cab[2]))
        else:
            cabs_list.append(Hatchback(current_cab[0], current_cab[1], current_cab[2]))
    return cabs_list


cabs = read_file('cabs.txt')
num = 1
for curr_cab in cabs:
    if curr_cab.get_type_of_cab() == 'Sedan':
        print(f'Sedan {num} will pay {curr_cab.calculate_fare()} TL')
        num += 1

print(f'\nThere are {find_greater(cabs, comp_cab)} Sedan cars newer than 2015\n')

total_km = 0
for curr_cab in cabs:
    if curr_cab.get_type_of_cab() == 'Hatchback' and curr_cab.get_year() == 2020:
        total_km += curr_cab.get_kms()

print(f'All Hatchback cars of year 2020 have travelled {total_km} kms')
