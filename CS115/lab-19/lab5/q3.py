class Movie:
    def __init__(self):
        self.movie_dict = {}
    # 1998,Life is Beautiful

    def load_movies(self, filename):
        movies = open(filename, 'r')
        for line in movies:
            curr_movie = line.split(',')  # movie year, movie name
            curr_movie[1] = curr_movie[1][:-1:]
            if curr_movie[1][0] in self.movie_dict:
                self.movie_dict[curr_movie[1][0]].append((curr_movie[0], curr_movie[1]))
            else:
                self.movie_dict[curr_movie[1][0]] = [(curr_movie[0], curr_movie[1])]

    def get_movies_by_year(self, year):
        movie_list = []
        for i in self.movie_dict:
            for j in range(len(self.movie_dict[i])):
                if self.movie_dict[i][j][0] == year:
                    movie_list.append(self.movie_dict[i][j][1])
        return movie_list

    def get_movies_by_name(self, char):
        movie_list = []
        for i in self.movie_dict:
            if i == char:
                movie_list.append(self.movie_dict[i])
        return movie_list

    @staticmethod
    def print_list(given_list):
        for i in range(len(given_list)):
            if type(given_list[i]) == list:
                for j in range(len(given_list[i])):
                    print(given_list[i][j])
            else:
                print(given_list[i])


movie = Movie()
movie.load_movies('movie_data.csv')
movie.print_list(movie.get_movies_by_name(input('Enter first character of movies to search: ')))
movie.print_list(movie.get_movies_by_year(input('Enter year to search: ')))
