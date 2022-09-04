# searching in arrays

# importing relevant modules
import numpy as np

# finding a giving value in arrays

# 1d array
a1 = np.array([1,2,3,4,5,6,4,3,2,1])
print(len(a1))
#finding given value in above element
x = np.where(a1 == 4)
y = np.where(a1%2 == 0)
z= np.where(a1 < 2)
print(x)
print(y)
print(z)
