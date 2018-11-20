import numpy as np
b = 20
c = 5

a = np.sqrt((b**2) + (c**2))

print(str(a))

print('a has the type ' + str(type(a)) + ' while b and c have the types respectively ' + str(type(b)) + ' and ' + str(type(c)))

#lets convert a into an integer

a_int = int(a)
print('with the integer type applied a is now ' + str(type(a_int)))

#purposeful error below

#print(a + " squared equals " + b + " squared + " + c + " squared.")

#this is clearly worong as print attempts to print strings only and the variables are type integer

#the fixed line is below 
print(str(a) + " squared equals " + str(b) + " squared + " + str(c) + " squared.")



exit 
