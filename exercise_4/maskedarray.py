import numpy.ma as MA

mask = MA.masked_array(range(0,9), fill_value = -999, mask = [0, 0, 0, 1, 0, 0, 0, 0, 0])
print(mask)


