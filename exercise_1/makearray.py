import numpy as np

x = list(range(1,11))
a1 = np.array(x, dtype = np.int32)
a2 = np.array(x, dtype = np.float32)

print(a1.dtype)

