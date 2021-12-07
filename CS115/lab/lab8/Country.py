# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:14:18 2020

"""


class Country:
    def __init__(self, cName, continent, life_m, life_f):
        self.__country = cName
        self.__continent = continent
        self.__life_male = float(life_m)
        self.__life_female = float(life_f)
        
    def getCountry(self):
        return self.__country
        
    def getContinent(self):
        return self.__continent
    
    def getLifeMale(self):
        return self.__life_male

    def getLifeFemale(self):
        return self.__life_female
    
    def calculate_average(self):
        return (self.__life_male + self.__life_female) / 2
           
    def __str__(self):
        s = 'Country:' + self.__country + '\n'
        s += 'Average Life Expectancy: ' + str(self.calculate_average()) + '\n'
        
        return s
        
    def __repr__(self):
        s = 'Country:' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n' 
        s += 'Life Expectancy for Males: ' + str(self.__life_male) + '\n'
        s += 'Life Expectancy for Females: ' + str(self.__life_female) + '\n'
        
        return s
    
    def __eq__(self, other):
        return self.getCountry() == other.getCountry()
        
        
        
        
        
    
    
