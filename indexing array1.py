# Indexing arrays

# importing relevant modules
import numpy as np

# Let's start indexing arrays
array = np.array([1, 2, 3, 4, 5]) # 1d array
print(array[0]) # returns 1st element in array

# 2d indexing
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim[0, 0]) # returns 1st element in 1st dimension
print(two_dim[1, 1]) # returns 2nd element in 2nd dimension

# 3d indexing
three_dim = np.array([[[1,2,3], [4, 5, 6], [7,  8, 9]]])
print(three_dim[0, 1, 2])
