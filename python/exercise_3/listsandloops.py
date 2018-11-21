#ESKETIT
forward = []       #created two empty lists
backward = []
values = ["a", "b", "c"]
for i in values:
    forward.append(i)      #for each value in values i have appended forward
    backward.insert(0, i)   #backward has these values in reverse order
print(str(forward))
print(str(backward))

forward.reverse() #I then switch the order of forward to backward
print(str(forward))
if forward == backward:
    print('eskeetit')   #and check that the order is the same


