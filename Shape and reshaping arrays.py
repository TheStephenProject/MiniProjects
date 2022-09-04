# Shape and reshaping arrays

# importing relevant modules
import numpy as np

# shape of an array
array = np.array([[1, 2, 3]])
print(array.shape) # prints the dimensions m x n
# fails when array is not symmetric

# Reshaping arrays
# suppose w ehave an array of student's ages and we
# have 3 students of each age
students = np.array([19, 19, 19, 20, 20, 20, 21, 21 ,21])
# we also have their average exam score over the year
exam_score = np.array([57, 60, 65, 59, 63, 70, 65 ,72, 75])
# splitting up exam score
exam_split = exam_score.reshape(3, 3)
print(exam_split)

# can't reshape every single array
# i.e. exam_split = exam_score.reshape(2, 4)
# will not work must equal total elements in array

# reshape different dimensions
one_dim = np.array([1, 2, 3, 4, 5, 6])
three_dim = one_dim.reshape(2,3, 1)
print(three_dim)
# this takes one_dim and breaks it into 2 arrays
# each will have 3 arrays
# made up of 1 element