#recall wth open("file", 'r') as whatever (the file object):
#if we wish to use the data, take the data into string with whatever.read() 
#we don't need tgo close the file as with only opens while the function operates
#read argument can take a byte / character number to read max

#instead of characters we can use readline() to read each file line 
#while line !='': keep looping until no more left
#otherwise to read all lines use readlines()
#then we can switch out while for a for loop over all lines


#when writing files we can use write or writelines
#\n is new line flag



