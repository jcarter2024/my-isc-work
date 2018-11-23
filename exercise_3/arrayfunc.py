import numpy as np
import sys
#need to feed in array and produce added array 
#define a 2*2 array for testing


def magnitude(a, b):
    a=1
    b=3
    m = np.sqrt(a**2 + b**2)
    return m
 
def array_check(u, v):    #takes two arguments array u and array v

    final_array = magnitude(u, v)
    print(final_array)

    magnitude_condition1 = final_array < 0.1
    result = (np.where(magnitude_condition1, 0.1, final_array))
    print(result)
    return result
