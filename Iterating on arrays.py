# Iterating on arrays
# importing relevant modules
import numpy as np

# creating a 1d array
one_dim = np.array([1, 2, 3, 4, 5])
# iterating over 1d array
for element in one_dim:
    print(element) # will prent each element in array
# creating a 2d array
two_dim = np.array([[1, 2, 3], [4, 5,6]])
# iterating over 2d array
for element in two_dim:
    print(element)
# notice how it doesn't produce the individual numbers

# to produce numbers

for element in two_dim:
    for number in element:
        print(number)
# short-cut for higher d arrays
# using 'nditer'
for element in np.nditer(two_dim):
    print(element)

# figuring out the index - using 'ndenumerate'
for index, element in np.ndenumerate(two_dim):
    print(index, element)