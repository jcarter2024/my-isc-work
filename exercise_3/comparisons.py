import numpy as np 

arr = np.array(range(0, 10))
if arr.size < 3:
    print('less than 3 if condition')

print(np.logical_or(arr <3, arr < 8 ))

condition = np.logical_or(arr <3, arr < 8 )
print(np.where(condition, arr * 5, arr * -5))



