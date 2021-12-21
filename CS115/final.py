import numpy as np
import matplotlib.pyplot as plt

# Using the appropriate functions, generate two
# numpy arrays, one that stores quarters
# (one to four) and second that
# stores the prices: [9.25, 23.6, 35.87, 22.5]

a1 = np.arange(1, 4.1)
prices = np.array([9.25, 23.6, 35.87, 22.5])

# Prices fluctuate between -2 and 5 each quarter.
# Generate an array with random values to represent
# the fluctuations each quarter.
# Hint: numpy’s random.rand(n) function
# returns n values between 0 and 1.

fluctuate = -2 + 7 * np.random.rand(prices.size)

# Create a new array that stores the
# updated prices (price + fluctuation).

updated_prices = prices + fluctuate

# Display the prices, fluctuations and the updated prices.

print(f'Prices: {prices}\nFluctuations: {fluctuate}\nUpdated Prices: {updated_prices}')

# Using the arrays defined above, create the following plot.
# Pay attention to details such as labels,etc.

plt.clf()
plt.title('Comparison of Stock Prices and Fluctuation')
plt.subplot(2, 1, 1)
plt.plot(a1, prices, a1, fluctuate)
plt.ylabel('Prices')
plt.legend(['Starting Prices', 'Fluctuation'])

plt.subplot(2, 1, 2)
plt.plot(a1, updated_prices)
plt.ylabel('Updated Prices')
plt.xlabel('Quarters')
plt.show()


# Write a function, max_chars() that takes a 2D list of strings as
# a parameter and returns a list containing the maximum length of
# the strings in each column.

# SampleData (sentences may change):
# sentences = [['lion', 'house', 'car'],
#              ['cat', 'dog', 'car'],
#              ['cat', 'house', 'dragon']]
# max_chars(sentences) returns [4, 5, 6]


def max_chars(table):
    size_list = []
    for i in range(len(table[0])):  # for tracing columns
        curr_max = 0
        for j in range(len(table)):  # row wise tracing
            if curr_max < len(table[j][i]):
                curr_max = len(table[j][i])
        size_list.append(curr_max)
    return size_list


# Create a Time class with the following data and methods.
# All attributes should be private and should be named appropriately.
# a. __init__ method should initialize the hours and minutes to
# the values passed as parameters. All data members should be private.
# b. Method addTime() which updates the Time (hours and minutes) with
# the minutes passed as an int parameter. E.g. (2 hour and 50 min) + (80 minutes) is (4 hr and 10 min)
# c. Method __lt__() that compares two Time objects, and
# returns True if the time is earlier than the parameter time, False if not.
# d. Method __repr__() which returns a string representation of the time in the following format: 08:40

class Time:
    def __init__(self, hours, minutes):
        self.__hours = (int(hours) + (int(minutes) // 60)) % 24
        self.__minutes = int(minutes) % 60

    def add_time(self, time_pass):
        self.__minutes += time_pass
        self.__hours += self.__minutes // 60
        self.__minutes = self.__minutes % 60

    def __lt__(self, other):
        return self.__hours * 60 + self.__minutes < other.__hours * 60 + other.__minutes

    def __repr__(self):
        hour = f'0{self.__hours}' if self.__hours < 10 else hour = f'{self.__hours}'
        minutes = f'0{self.__minutes}' if self.__minutes < 10 else hour = f'{self.__minutes}'
        return f'{hour}:{minutes}'


# Create a python script that does the following:
# a. Create an empty list named appointments, which will store appointment Times for a doctor.
# b. Using data from the file, schedule_times.txt, store each Time object in the appointments list.
# c. Sort the list of times.
# d. The doctor may be delayed, and will have to postpone her/his appointments for the day from
# the morning (starting at 8:30) or the afternoon(starting at 12:30). Your script should input from the user when the delay will start, and the number of minutes to delay. You should then update all times in the list using the appropriate functionality.
# e. Display the updated list of times.
# f. Input a name of a Lab Test to search for, and using the Patient functionality, display the lab
# result value for each Patient in the list whose result for the input lab test is out of range.

# unfortunately this great code below is not allowed to use since they don't teach it in class :(
form = lambda x, y=':', i=0: x.split(y)[i].strip()
appointments = [Time(form(x), form(x, i=1)) for x in open('schedule_times.txt', 'r')]
#   ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###   #

# and this is the allowed garbage
file = open('schedule_times.txt', 'r')
appointments1 = []
for time in file:
    h_m = time.split(':')
    hours = h_m[0]
    minutes = h_m[1].strip()
    appointments1.append(Time(int(hours), int(minutes)))
file.close()


appointments.sort()

time = input('When will delay start (M)orning / (A)fternoon: ')
minute = int(input('How many minutes will the doctor be late: '))

m = Time(8, 30)
a = Time(12, 30)
for app in appointments:
    if time == 'M':
        if m < app < a:
            app.add_time(minute)
    elif time == 'A':
        if a < app:
            app.add_time(minute)

print('Scheduled appointments:', appointments)
