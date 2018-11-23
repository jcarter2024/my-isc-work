import numpy as np

arr= np.array((range(4), range(10, 14)))
print(arr.reshape(2, 2, 2))
print(np.transpose(arr))

print(arr.flatten())
print(np.array(arr, dtype = 'float32'))

