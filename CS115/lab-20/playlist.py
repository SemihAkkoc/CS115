# not finished yet

class Playlist:
    def __init__(self, name, purpose, length):
        self.__name = name
        self.__purpose = purpose
        self.__length = length
        self.__song_list = []

    def get_song(self, index):
        return self.__song_list[index]

    def get_num_songs(self):
        return self.__length

    def add_song(self, song):
        self.__song_list.append(song)
        self.__length = len(self.__song_list)

    def bubble_sort(self):
        song_duration = []
        for i in range(len(self.__song_list)):
            song_duration.append((self.__song_list[i].get_duration(), i))
        song_duration.sort(reverse=True)
        for e in song_duration:
            self.__song_list[e[1]] = e[0]

    def sort_playlist(self):
        self.__song_list.sort()

    def binary_search(self, duration, start, end):
        self.bubble_sort()
        list_search = self.__song_list[start:end+1]
        wanted_list = []
        while len(list_search) > 0:
            if list_search[len(list_search)//2] > duration:
                pass

