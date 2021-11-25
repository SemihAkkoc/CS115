class Person:
    def __init__(self, name, age, gender, location):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__location = location

    def __repr__(self):
        return repr(self.__name + ' is the name, ' + self.__age + ' is the age, and ' + self.__gender + ' is the gender and ' + self.__location + ' location')

    def name(self):
        return self.__name

    def age(self):
        return self.__age

    def gender(self):
        return self.__gender

    def location(self, new_location=''):
        if new_location:
            self.__location = new_location
        return self.__location

    def increase_age(self, increase_step=1):
        self.__age += increase_step


def get_by_location(person_list, location):
    new_person_list = []
    for person in person_list:
        if person.location() == location:
            new_person_list.append(person)
    return new_person_list


def get_by_gender(person_list, gender):
    new_person_list = []
    for person in person_list:
        if person.gender() == gender:
            new_person_list.append(person)
    return new_person_list


file = open('input.txt', 'r')
people = []

for line in file:
    curr_person = line.split(',')
    curr_person[-1] = curr_person[-1][:-1:]
    people.append(Person(curr_person[0], curr_person[1], curr_person[2], curr_person[3]))

gender_list = get_by_gender(people, 'female')
location_list = get_by_location(people, 'ankara')

print('*'*8 + 'Printing Females in Ankara' + '*'*8)
for person in gender_list:
    if person in location_list:
        print('Name:', person.name() + '\nAge:', person.age() + '\nGender:', person.gender() + '\nLocation:', person.location() + '\n')


