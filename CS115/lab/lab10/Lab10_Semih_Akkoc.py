import numpy as np
import matplotlib.pyplot as plt

weight = np.array([2, 3, 4, 5, 10, 16, 22, 26])  # candle weight (oz)
time = np.array([15, 20, 35, 36, 80, 100, 120, 180])  # burning time (hours)

plt.clf()
plt.figure(1)
plt.title('Burning Time of Candle')
plt.plot(weight, time, ' bo')
plt.xlabel('Weight of Candle')
plt.ylabel('Burning Time')

c = np.polyfit(weight, time, 1)
points = [c[0]*x+c[1] for x in weight]
plt.plot(weight, points, 'r-')

student = np.loadtxt('students.txt', dtype=int, skiprows=1)
full = student[student[:, 0] == 1]

plt.figure(2)  # 1: histogram, 2: plot, 3: pie chart, 4: bar chart

# 1: histogram
plt.subplot(2, 2, 1)
plt.title('Frequency of Math Gr. of Full Sc. Students')
plt.hist(full[:, 1], 3)  # with 3 bins

# 2: plot chart
plt.subplot(2, 2, 2)
plt.title('Reading vs Writing Gr. of Full Sc. Students')
num_full = [x for x in range(1, len(full[:, 0])+1)]
plt.plot(num_full, full[:, 2], 'dr-.', num_full, full[:, 3], 'sk--')
plt.ylabel('Grades')
plt.legend(['Reading', 'Writing'])

# 3: pie chart
plt.subplot(2, 2, 3)
plt.title('Scholarship Percentages')
scholarship = [np.where(student[:, 0] == 1)[0].size, np.where(student[:, 0] == 2)[0].size, np.where(student[:, 0] == 3)[0].size]
plt.pie(scholarship, labels=['Full', 'Half', 'None'], autopct='%1.1f%%')

# 4: bar chart
plt.subplot(2, 2, 4)
plt.title('Comparison of Math Grades: Full Sc. vs All Students')
plt.bar('Full-sc.', np.mean(full[:, 1]), width=0.75)
plt.bar('All', np.mean(student[:, 1]), width=0.75)
plt.ylabel('Average of Grades')
plt.show()

# this was a great journey I liked doing lab assignments truth to be told I was looking forward to thursdays to come
# however, now we need to wrap this up. To summarize I can say that I had some bad and good experiences with lab questions
# nevertheless, I am glad that I have taken this course, and I believe I have improved myself.
# take care - see you in new projects
