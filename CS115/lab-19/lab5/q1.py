def fill_list(min_val, max_val):
    from random import randint
    given_list = []
    is_duplicate = False
    while not is_duplicate:
        curr_val = randint(min_val, max_val)
        if not (curr_val in given_list):
            given_list.append(curr_val)
        else:
            is_duplicate = True
    return given_list


def update_elements(given_list):
    new_list = [given_list[0]]
    for i in range(1, len(given_list)-1):
        curr_val = 0
        if given_list[i] >= given_list[i+1]:
            curr_val = given_list[i]
        else:
            curr_val = given_list[i+1]
        if curr_val <= given_list[i-1]:
            curr_val = given_list[i-1]
        new_list.append(curr_val)
    new_list.append(given_list[-1])
    return new_list


L1 = fill_list(int(input('Enter lower bound: ')), int(input('Enter upper bound: ')))
print('Original list: ', L1)
L2 = update_elements(L1)
print('New list: ', L2)
