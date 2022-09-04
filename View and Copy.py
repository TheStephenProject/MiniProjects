# copy and view

# importing relevant modules
import numpy as np

## copy
array = np.array([1, 2, 3, 4, 5]) #1d array
copy = array.copy() # creates copy of above array
print(copy)
print(array)

# changing array and using
A2 = np.array([1, 2, 3])
copy1 = A2.copy()
A2[0] = 10
print(A2)
print(copy1) #copy retains original

# view
A3 = np.array([1, 2, 3])
view = A3.view()
A3[0] = 10
print(A3)
print(view) # view changes as it's assigned state changes

print(view.base) # returns the array(changes)
print(copy1.base) #returns None