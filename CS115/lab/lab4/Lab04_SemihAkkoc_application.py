from Lab04_SemihAkkoc_module import *

city = input('Enter city to search (“quit” to exit): ')
print()

while city.lower() != 'quit':
    city_districts = open('city_districts.txt', 'r')
    city_pop_area = open('city_data.txt', 'r')
    search_city = open('search_city_density.txt', 'w')

    if not district_density(city, city_districts, city_pop_area, search_city):
        print(f'{city} not found...\n')
    else:
        search_city.close()
        search_city = open('search_city_density.txt', 'r')
        limit = float(input('Enter maximum density: '))
        curr_district_names = find_district(limit, search_city)
        if curr_district_names:
            print(f'Districts in {city} with population density below {limit}:')
            print(curr_district_names)
        else:
            print(f'No districts in {city} with population density below {limit:.1f}\n')
        search_city.close()

    city = input('Enter city to search (“quit” to exit): ')
    print()

    search_city.close()
    city_districts.close()
    city_pop_area.close()

print('Thank you - Goodbye')  # this was a really good lab assignment
