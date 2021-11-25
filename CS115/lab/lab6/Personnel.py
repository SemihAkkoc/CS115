class Personnel:
    def __init__(self, id_num, name, department, status, salary):
        self.__id_num = int(id_num)
        self.__name = name
        self.__department = department
        self.__status = status
        self.__salary = int(salary)
        self.increase_salary()

    def get_id(self):
        return self.__id_num

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_status(self):
        return self.__status

    def get_salary(self):
        return self.__salary

    def increase_salary(self):
        if self.get_status() == 'M':
            self.__salary = self.get_salary() * 1.12
        elif self.get_status() == 'A':
            self.__salary = self.get_salary() * 1.15
        else:
            self.__salary = self.get_salary() * 1.18

    def __str__(self):
        repr_str = 'Id: ' + str(self.get_id()) + '\n'
        repr_str += 'Department: ' + str(self.get_department()) + '\n'
        repr_str += 'Salary: ' + str(self.get_salary()) + 'TL\n'
        return repr_str

    def __repr__(self):
        repr_str = 'Id: ' + str(self.get_id()) + '\n'
        repr_str += 'Name: ' + str(self.get_name()) + '\n'
        repr_str += 'Department: ' + str(self.get_department()) + '\n'
        repr_str += 'Status: ' + str(self.get_status()) + '\n'
        repr_str += f'Salary: {self.get_salary():.1f} TL\n'
        return repr_str


def read_file(filename):
    personnel_list = []
    personnel_dict = {}
    file = open(filename, 'r')

    for line in file:
        curr_personnel = line.split(',')
        curr_personnel[-1] = curr_personnel[-1].strip()
        # creating personnel objects and adding them to the list
        personnel_list.append(Personnel(curr_personnel[0], curr_personnel[1], curr_personnel[2], curr_personnel[3], curr_personnel[4]))

    print('All personnel:\n', personnel_list)

    for person in personnel_list:
        if person.get_status() == 'B':
            personnel_dict[person.get_id()] = person

    print('Personnel With Both Managerial and Academic Responsibilities:')
    for person in personnel_dict:
        print(personnel_dict[person])


read_file('personnel.txt')
