def search(string, char=' '):
    """
    this function return the index of desired character

    Parameters:
           string (str): A string
           char (str): a character
    Returns:
           (int): returns index of desired character
    """

    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1


c = open('lab/lab4/city_districts.txt', 'r')
p = open('lab/lab4/city_data.txt', 'r')

l = input('enter city: ')
for line in c:
    curr_pop_area = p.readline()
    print(curr_pop_area[:search(curr_pop_area):].rstrip())
    print(curr_pop_area[search(curr_pop_area) + 1:len(curr_pop_area) - 2:].rstrip())
    """
    if line.lower()[:search(line):] == l.lower():
        curr_density = float(curr_pop_area[:search(curr_pop_area):]) / float(curr_pop_area[search(curr_pop_area) + 1:len(curr_pop_area) - 2:])
        curr_dist_density = f'{line[search(line) + 1:len(line) - 2:]},{curr_density:.1f}\n'
        #print(curr_dist_density)
    """