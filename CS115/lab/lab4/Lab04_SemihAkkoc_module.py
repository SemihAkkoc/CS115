"""
This programme contains the necessary methods-functions
"""


def search(string, char='\t'):
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


def district_density(city_name, inp_city_names, inp_city_pop, res):
    """
    takes city names file and population and area files then it
    calculates the density of each district in wanted city then
    writes the current districts in result file

    Parameters:
           city_name (str): name of the city
           inp_city_names (file): the file that contains city names
           inp_city_pop (file): the file that contains city population and area
           res (file): file to write the density results
    Returns:
           is_city (bool): True or False depending on whether city exists in the file or not
    """

    is_city = False
    # searching in given file line by line
    for line in inp_city_names:
        curr_pop_area = inp_city_pop.readline()  # assigning the current population and area value

        # checking if the current city is the city desired
        if line[:search(line):].lower() == city_name.lower():
            # calculating the density and writing in the result file
            curr_pop_area = curr_pop_area.replace(',', '')
            curr_density = float(curr_pop_area[:search(curr_pop_area):]) / float(curr_pop_area[search(curr_pop_area)+1::].rstrip())
            curr_dist_density = f'{line[search(line)+1::].rstrip()},{curr_density:.1f}\n'
            res.write(curr_dist_density)
            is_city = True
    return is_city


def find_district(limit, density_file):
    """
    this function returns the string of district names if
    district density is below the limit value

    Parameters:
           limit (float): limit of the density
           density_file (file): the file to search into
    Returns:
           curr_districts (str): returns the wanted string
    """

    curr_districts = ''
    for line in density_file:
        if float(line[search(line, ',')+1::].rstrip()) < limit:
            curr_districts += line[:search(line, ','):] + '\n'
    return curr_districts
