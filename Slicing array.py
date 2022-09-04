# slicing array
# importing relevant modules
import numpy as np

# slicing 1d array
one_dim = np.array([1, 2, 3, 4, 5])
print(one_dim[0:3])
print(one_dim[:2]) # assumes 0 for blank space
# can recall elements in steps
print(one_dim[0:4:2]) # [x ,y z], x = start, y = end, z= steps

# 2d array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
# this will return from 1st element to the 2nd element
# from 2nd dimension, [4 5]
print(two_dim[1, 0:2])

# look at this
two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# reverse of above, returns
# 1st element of 1st and 2nd dimension
print(two_dim2[0:2, 0])