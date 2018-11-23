import numpy as np

listy = [2, 3.2, 5.5, -6.4, -2.2, 2.4]
a = np.array(listy)
print(a[1])
print(a[1:4])

list2 = [[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]]
a2 = np.array(list2, dtype = np.float32)
print(a2)
print(a2[1, 2]) #all rows third column
print(a2[1:4, 0:4]) #rows 2-4, columns 1-4
#print(a[1:, 2]) #row 1 onwards column 2

