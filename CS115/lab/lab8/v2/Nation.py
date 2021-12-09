# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:14:18 2020

"""

class Nation:
    def __init__(self, cname, continent, pop, sa):
        self.__country = cname
        self.__continent = continent
        self.__population = float(pop)
        self.__surface_area = float(sa)
        self.__density = self.calculate_density()
        
    def getCountry(self):
        return self.__country
        
    def getContinent(self):
        return self.__continent
    
    def getPopulation(self):
        return self.__population
    
    def getSurface_area(self):
        return self.__surface_area
    
    def getDensity(self):
        return self.__density

    def calculate_density(self):
        return self.__population / self.__surface_area

    def __lt__(self, other):
        return self.getCountry() <= other.getCountry()

    def __eq__(self, other):
        return self.getCountry() == other.getCountry()

    def __str__(self):
        s = 'Country: ' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n' 
        s += f'Density: {self.__density:.2f}' + '\n'
        return s
    
    def __repr__(self):
        s = 'Country: ' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n' 
        s += f'Population: {self.__population:.1f}' + '\n'
        s += f'Area: {self.__surface_area:.1f}' + '\n'
        s += f'Density: {self.__density:.2f}' + '\n'
        return s
