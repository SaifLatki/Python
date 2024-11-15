import numpy as np #import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #create a 1D array

print(f'Index from 1 to 5 exclude 0 index= {arr[1:5]}') #print the array from index 1 to 5
print(f'Index from 4 to last exclude 4 index= {arr[4:]}') #print the array from index 4 to the end
print(f'Index from 0 to 4 exclude after 4 index= {arr[:4]}') #print the array from the start to index 4
print(f'Index from last -3 to last -1= {arr[-3:-1]}') #print the array from index -3 to -1