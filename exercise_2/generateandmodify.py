import numpy as np

#this programme is for making some modifications to a generated array 

arr= np.array((range(4), range(10, 14))) #first we make an array of 2 rows, each row has elements of the given range 
                                         #and demonstrate that this can be done with the range function
#print(arr)

print(arr.reshape(4, 1, 2)) #we can reshape the array into 3 dimensiions (rows, depth, columns)
print(np.transpose(arr)) #simple transpose operation

print(arr.flatten()) #make simple row vector
print(np.array(arr, dtype = 'float32')) #make float 

