# haven't finished bekir interrupted me

class Doctor:
    def __init__(self, name, title):
        self.__doc_name = name
        self.__title = title

    def get_doc_name(self):
        return self.__doc_name

    def get_title(self):
        return self.__title

    def set_doc_name(self, name):
        self.__doc_name = name

    def set_title(self, title):
        self.__title = title

    def __eq__(self, other):
        return self.__doc_name == other.__doc_name and self.__title == other.__title

    def __lt__(self, other):
        if self.__title < other.__title:
            return self
        elif self.__title > other.__title:
            return other
        else:
            if self.__doc_name < other.__doc_name:
                return self
            elif self.__doc_name > other.__doc_name:
                return other

