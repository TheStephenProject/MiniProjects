# basic operations on arrays

# importing relevant module
import numpy as np

# we can create an array between numbers
# like one can do in a list and range command

a = np.arange(0, 5)
print(a)
# compare with
A = list(range(0, 5))
print(A)

# mathematical function
b = np.array([4, 6, 19, 23, 45])
# adding
print(a + b)
# subtracting
print(a-b)
print(b-a)
# square all the elements in the array
print(a*a)
print(a**2)

# NumPy inbuilt functions
print(np.sqrt(a**2)) #produces a
# floats are produced

# multiplying array 'a' by 3
print(a*3)
# dividing
print(a/2)

# booleans with arrays
c = np.array([1,2, 3, 4,])
print(c < 2)

