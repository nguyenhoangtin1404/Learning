# library
import matplotlib.pyplot as plt

# create data: an array of values
size_of_groups = [12, 11, 3, 30]

# Create a Figure and an Axes # Initialize layout
fig, ax = plt.subplots()

# show value in pie chart # autopct='%1.1f%%' means show value in percentage
ax.pie(size_of_groups, autopct='%1.1f%%')
# show legend
ax.legend(['A', 'B', 'C', 'D'])
# show title
ax.set_title('Pie Chart')

plt.show()
