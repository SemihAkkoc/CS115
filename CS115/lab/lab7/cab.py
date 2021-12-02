class Cab:
    def __init__(self, type_of_cab, kms, year):
        self.__type_of_cab = type_of_cab
        self.__kms = int(kms)
        self.__year = int(year)

    def get_kms(self):
        return self.__kms

    def get_type_of_cab(self):
        return self.__type_of_cab

    def get_year(self):
        return self.__year

    def __gt__(self, other):
        return self.__year > other.get_year() and self.__type_of_cab == other.get_type_of_cab()

    def __eq__(self, other):
        return self.__year == other.get_year() and self.__type_of_cab == other.get_type_of_cab()

    def __repr__(self):
        pass


class Sedan(Cab):
    def __init__(self, type_of_cab, kms, year):
        Cab.__init__(self, type_of_cab, kms, year)
        self.__price_per_km = 2.5

    def calculate_fare(self):
        return self.__price_per_km * self.get_kms()


class Hatchback(Cab):
    def __init__(self, type_of_cab, kms, year):
        Cab.__init__(self, type_of_cab, kms, year)
        self.__price_per_km = 2.2

    def calculate_fare(self):
        return self.__price_per_km * self.get_kms()
