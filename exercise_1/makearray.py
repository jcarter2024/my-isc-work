import numpy as np

x = list(range(1,11)) #create a list from/inc 1 to notinc 11
print(x)

a1 = np.array(x, dtype = np.int32) #make the list into array, data type integer
print(a1)
a2 = np.array(x, dtype = np.float32)#make the list into array, data type float
print(a2)

print("the first array is the built with data type "+str(a1.dtype)+ \
      ", whereas the second array is built with data type " + str(a2.dtype)) 


