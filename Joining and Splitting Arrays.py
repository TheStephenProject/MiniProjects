# Joining and Splitting Arrays
# importing relevant modules
import numpy as np

# joining arrays

# creating 2 1D arrays
array1 = np.array([1, 2, 3, 4, 5,])
array2 = np.array([6, 7, 8, 9, 10,])
# concatenating the two above arrays
joined_array = np.concatenate((array1, array2))
print(joined_array)

# join arrays along rows
array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([[7, 8, 9], [10, 11, 12]])
print(array3)
print(array4)
joined_row_array = np.concatenate((array3, array4), axis=1)
print(joined_row_array)
# recall axis=1 corresponds to rows

#splittng array
# 1d array
arr = np.array([1, 2, 3, 4, 5, 6])
split_array = np.array_split(arr, 3)
print(split_array)
# recall elements from split_array
print(split_array[0])
print(split_array[1])
print(split_array[2])