# importing numpy
import numpy as np

# 0D Array
zero_dim= np.array(1)
print(zero_dim)

# printing 1d array
one_dim = np.array([1, 2, 3, 4, 5])
print(one_dim)

# 2d array
two_dim = np.array([[1 ,2 ,3], [4, 5, 6]])
print(two_dim)

# 3d array
three_dim = np.array([[[1 ,2 ,3], [4, 5, 6], [7,8,9], [10, 11, 12]]])
print(three_dim)

# notice how the number of brackets increases

# how to find the dimension of a given array
print(two_dim.ndim)

# how to create any sized array
new_array = np.array(17, ndmin=5)
print(new_array)