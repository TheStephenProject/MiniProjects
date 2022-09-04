# data analysis

# importing relevant modules
import numpy as np

# operations
one_dim = np.array([1, 2, 3, 4, 5])
two_dim = np.array([[1,2,3], [4,5,6]])
two_dim2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# summations
print(sum(one_dim)) # produces 15
print(sum(two_dim)) # adds up corresponding elements in dimensions
# how to find total sum regardless of dimensions
print(one_dim.sum())
print(two_dim.sum())

# max and min
print(one_dim.min())
print(one_dim.max())
print(two_dim.max())



# 3d array operations - review
print(two_dim2.sum(axis=0)) #sum of columns
print(two_dim2.sum(axis=1)) #sum of row

#print(three_dim)