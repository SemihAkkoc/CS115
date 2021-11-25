def is_spaced(password):
    for i in range(len(password) - 2):
        if abs(int(password[i]) - int(password[i + 1])) == abs(int(password[i + 1]) - int(password[i + 2])):
            return True
    return False


def contains_birthyear(password, birth_year):
    birth_year_str = str(birth_year)
    check_str, check_str2, j = '', '', 0
    for i in range(len(password)):
        if password[i] == birth_year_str[j] and not (password[i] in check_str):
            check_str += f'{password[i]}:'
            check_str2 += f'{i}:'
            j += 1
            if len(check_str2) >= 8:
                return True
    return False


def is_valid_password(password, birth_year):
    if len(password) < 3:
        return False
    else:
        try:
            int(password)
        except ValueError:
            return False

        if is_spaced(password):
            return False

        if contains_birthyear(password, birth_year):
            return False

        return True


password = input('Enter password: ')
year = int(input('Enter year of birth: '))
while not is_valid_password(password, year):
    print(password, 'is not a valid password - try again\n')
    password = input('Enter password: ')
    year = int(input('Enter year of birth: '))

print('Thank you - password is valid')