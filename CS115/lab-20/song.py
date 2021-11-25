class Song:

    def __init__(self, title, artist, duration):
        self.__title = title
        self.__artist = artist
        self.__duration = int(duration)

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def __repr__(self):
        return self.__title + ' ' + self.__artist + ' ' + str(self.__duration) + '\n'

    def __lt__(self, other):
        return self.__artist < other.get_artist()
