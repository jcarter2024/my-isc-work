import numpy as np
#this program makes some arrays 

a= np.zeros((2, 3, 4)) #2 arrays of dimension 3x4
print(a)
b = np.ones((2, 3, 4)) #same but for ones 
print(b)

c = np.arange((1000)) #arange returns a list of values 
print(c)
#arange by default begins at 0 and has 1 step interval, but this can be modified

d=np.arange(0, 1000, 1) #this is identically the same as above
print(d)

if c.all()==d.all():
    print("These arrays are identical!")
else:
    print("We have misunderstood the arange arguments")
    
    