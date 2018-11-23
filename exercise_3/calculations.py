import numpy as np

a = np.array((range(4), range(10, 14)))
print(a)
b = np.array([2, -1, 1, 0])
print(b)

c=a*b
print(c)
b1 = b*100
b2 = b*100.0
print(b1)
print(b2)

print(b1==b2)
print(a.typecode)

