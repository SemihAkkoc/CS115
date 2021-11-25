def count(string):
    new_dict = {}
    for c in string:
        if c != ' ':
            if not (c in new_dict):
                new_dict[c] = 1
            else:
                new_dict[c] += 1
    return new_dict


def find_ch_most(given_dict):
    curr_max = 0
    max_char = ''
    for key in given_dict:
        if given_dict[key] > curr_max:
            curr_max = given_dict[key]
            max_char = key
    return max_char


dict1 = count(input('Enter a sentence: '))
print('Character "' + str(find_ch_most(dict1)) + '" has occurred the most in given sentence')


def common(first_name, last_name):
    common_list = []
    for i in first_name:
        for j in last_name:
            if i == j and not (i in common_list):
                common_list.append(i)
    return common_list


def all_unique(first_name, last_name):
    unique_list = []
    for i in first_name:
        for j in last_name:
            if i != j and not (i in unique_list) and not (j in unique_list):
                unique_list.append(i)
                unique_list.append(j)
    return tuple(unique_list)


name = [i for i in input('Enter your name: ').split()]
print('common letters -> ', common(name[0], name[1]))
print('unique letters -> ', all_unique(name[0], name[1]))
