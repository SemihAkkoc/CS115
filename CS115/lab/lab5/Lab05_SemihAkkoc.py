# this program is used to store and retrieve year and title information about movies

def load_movies(filename):
    """
    return a dictionary where the keys are the integer years,
    and the values are a list of movies produced in that year.
    :param filename: file pointer
    :return: movie_dict: dictionary
    """

    movie_dict = {}
    for line in filename:
        curr_movie = line.split(',')  # movie year, movie name
        curr_movie[1] = curr_movie[1][:-1:]
        if int(curr_movie[0]) in movie_dict:
            movie_dict[int(curr_movie[0])].append(curr_movie[1])
        else:
            movie_dict[int(curr_movie[0])] = [curr_movie[1]]
    return movie_dict


def get_movies_by_year(movie_dict, year):
    """
    a list of the names of movies produced in the given year.
    If no movies exist, return an empty list.
    :param movie_dict: dictionary
    :param year: int
    :return: movie_list: a list that contains the wanted movies
    """

    movie_list = []
    for movie_year in movie_dict:
        if movie_year == year:
            movie_list.append(movie_dict[movie_year])
    if not movie_list:
        print(f'No movies from "{year}" found')
    else:
        print(f'Movies made in {year}:')
    return movie_list


def get_movies_by_keyword(movie_dict, keyword):
    """
    Return a list of tuples where each tuple contains the
     movie name and movie year for all movies whose name
     contains the given keyword.
    :param movie_dict: dictionary
    :param keyword: a string
    :return: movie_list: a tuple which contains wanted movies list
    """

    movie_list = []
    for movie in movie_dict:
        name = movie_dict[movie]
        for j in range(len(name)):
            if keyword in name[j]:
                movie_list.append((movie, name[j]))
    if not movie_list:
        print(f'No movies with the keyword "{keyword}" found')
    return tuple(movie_list)


def print_list(given_list):
    """
    with a given list this method prints the list
    :param given_list: a list
    :return: None
    """

    for movie in range(len(given_list)):
        if type(given_list[movie]) == list:
            for j in range(len(given_list[movie])):
                print(given_list[movie][j])
        else:
            print(given_list[movie])
    print()


# opening the file
movies = open('movie_data.csv', 'r')
# creating the dictionary
movie_dictionary = load_movies(movies)

# running this statement two times
for i in range(2):
    print_list(get_movies_by_year(movie_dictionary, int(input('Enter year to search: '))))
    print_list(get_movies_by_keyword(movie_dictionary, input('Enter keyword to search: ')))

# tbh this was a little bit easier problem when I compare it with other lab problems
