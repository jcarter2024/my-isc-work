x = [1, 2, 3, 4, 5]

print('Second item in list is ' + str(x[1]))
print('Second to last item in the list is ' + str(x[-2]))

y = (x[ : ]) 
print('full sliced list is ' + str(y))
z = (x[1:4])
print('list elements 2 to 4 are ' + str(z))

r=[]
for i in range(3,7): 
    r.append(i)
print(str(r))
