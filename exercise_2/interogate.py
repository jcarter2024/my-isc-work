import numpy as np

#lets make an array of 2 rows with elements in the given ranges
arr= np.array((range(4), range(-14, -10)))
print(arr.shape) #the array shape should be a 2x4
print(arr.size) #the size of the array should be 8 elements
print(arr.max()) #whats the maximum element value, its 13
print(arr.min()) #whats the minimum element value, its 0, for negatives it will show the lowest, i.e. no modulus
