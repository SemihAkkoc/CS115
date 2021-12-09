from Nation import Nation


def bubble_sort(nations_list):
    for i in range(len(nations_list) - 1):
        for j in range(len(nations_list) - i - 1):
            if nations_list[j].getContinent() + nations_list[j].getCountry() > nations_list[j+1].getContinent() + nations_list[j+1].getCountry():
                nations_list[j], nations_list[j + 1] = nations_list[j + 1], nations_list[j]


def search_country(nations_list, nation, s_index, e_index):
    if nations_list[s_index] < nation < nations_list[e_index]:
        if nations_list[(s_index + e_index)//2] == nation:
            return (s_index + e_index)//2
        elif nation < nations_list[(s_index+e_index)//2]:
            return search_country(nations_list, nation, s_index, (s_index+e_index)//2)
        else:
            return search_country(nations_list, nation, (s_index+e_index)//2, e_index)
    else:
        return -1


def read_countries(nations_list, filename):
    file = open(filename, 'r')
    for line in file:
        nation = line.split(';')
        nation[-1] = nation[-1].strip()
        nations_list.append(Nation(nation[0], nation[1], nation[2], nation[3]))


nations = []
read_countries(nations, 'nations.txt')
nations.sort()
print('Nations Sorted according to their names:\n', nations)
curr_nation = Nation(input('\nEnter the name of the country to search: '), '', 0, 1)
print(nations[search_country(nations, curr_nation, 0, len(nations)-1)])
bubble_sort(nations)
print('Nations Sorted according to their Continent and Name:\n', nations)
