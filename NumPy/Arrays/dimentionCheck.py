import numpy as np #import numpy as np

a = np.array([1, 2, 3, 4, 5]) #create a 1D array
b = np.array([[1, 2, 3], [4, 5, 6]]) #create a 2D array
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])#create a 3D array
d = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]]])#create a 4D array

print(f'a is {a.ndim} Dimentional Array') #print the number of dimensions of the array
print(f'b is {b.ndim} Dimentional Array') #print the number of dimensions of the array
print(f'c is {c.ndim} Dimentional Array') #print the number of dimensions of the array
print(f'd is {d.ndim} Dimentional Array') #print the number of dimensions of the array
