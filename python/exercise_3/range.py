y=[]
for i in range(1,11):   #create a list with range 1-10
    y.append(i)
print(str(y))

y[0] = 10    #change the first value in the list to value 10
print(str(y))

y.append(11) # added 11 to the list without modifying cuurent values
print(str(y))

y.extend(list(range(12,15))) #extended the list with another list [12, 13, 14]
print(str(y))

#you could also 'list' a range object.
my_list=list(range(1,11))
print(str(my_list))

