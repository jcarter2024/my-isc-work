import numpy as np

listy = [2, 3.2, 5.5, -6.4, -2.2, 2.4] #make a manual list
a = np.array(listy) #arrayify the list 
print(a[1]) #print the second element of a1
print(a[1:4]) #print the second element up to but not including the fifth

#lets make a list of lists 
list2 = [[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]]
a2 = np.array(list2, dtype = np.float32) #we arrayify the list of lists `and convert to floats 
#this places the lists as rows, and a new list on a separate column
print(a2)
print(a2[1, 2]) #print second row third element follow ([row, column]) format
print(a2[1:4, 0:4]) #rows 2-4, columns 1-4
print(a2[1:, 2]) #row 2 onwards (rows 2 and 3) column 2

