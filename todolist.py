import array as arr
import matplotlib.pyplot as plt
import pandas as pd
listNote = arr.array('u', ['a', 'b', 'c'])


def print_list_note():
    for n in listNote:
        print(n)


def add_note(p_string):
    listNote.append(p_string)


def remove_note(p_index):
    listNote.pop(p_index)


# add_note('d')
# remove_note(3)
# print_list_note()

# Create data
x = range(1, 6)
y = [1, 4, 6, 8, 4]

# Area plot
plt.fill_between(x, y)
plt.show()


# Create a data frame
df = pd.DataFrame(
    {'Group':  ['A', 'B', 'C', 'D', 'E'], 'Value': [1, 5, 4, 3, 9]})

# Create horizontal bars
plt.barh(y=df.Group, width=df.Value)

# Add title
plt.title('A simple barplot')
