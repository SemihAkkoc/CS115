from Country import Country


def selection_sort(countries):
    for i in range(len(countries)):
        curr_min = countries[i]
        for country in countries[i:]:
            if curr_min.getContinent() + curr_min.getCountry() > country.getContinent() + country.getCountry():
                curr_min = country
        countries.remove(curr_min)
        countries.insert(i, curr_min)


def search_countries(countries, continent, index):
    global continent_countries
    if continent == countries[index].getContinent():
        continent_countries.append(countries[index])
    if index != 0:
        search_countries(countries, continent, index-1)


def read_countries(filename):
    global countries
    file = open(filename, 'r')
    for line in file:
        country = line.split(',')
        country[-1] = country[-1].strip()
        countries.append(Country(country[0], country[1], country[2], country[3]))


continent_countries, countries = [], []

read_countries('country.txt')
continents = input('Enter continent to search: ')
print('List of Countries in', continents)
search_countries(countries, continents, len(countries)-1)
for country in continent_countries:
    print(country)

new_country_info = [x.strip() for x in input('Enter county name, continent, life expectancy for Men and life expectancy for Women: ').split(',')]
countries.append(Country(new_country_info[0], new_country_info[1], new_country_info[2], new_country_info[3]))
print('New Country added\n')
selection_sort(countries)
print('Countries by Continent and Name:\n', countries)
