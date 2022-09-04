# sorting arrays
#importing relevant modules
import numpy as np

# there's a sort function in numpy
# will sort array in mathematical order

array1 = np.array([1 ,123, 456, 321, 0 ,-2334, -2])
array1_sorted = np.sort(array1)
print(array1)
print(array1_sorted)

# sorting 2d arrays
array2 = np.array([[-4, 567, -23], [2453, -3535, 24]])
array2_sorted = np.sort(array2)
print(array2)
print(array2_sorted)

# Another cool function in NumPy - 'searchsorted'.
# This command will return the index where the inputted value
# would need to be placed in order to maintain order.
array3 = np.array([1, 3, 5, 6])
location = np.searchsorted(array3, 4)
print(location)

location2 = np.searchsorted(array3, [2, 4, 9])
print(location2)