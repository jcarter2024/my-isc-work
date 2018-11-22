#using the enumerate function

mylist = [23, "hi", 2.4e-10]
a = enumerate(mylist)
b = list(a)
for i in b:
    print(str(i))

#this almost completes the task but is in format (index, item)
#I need to switch the order of each tuple
#try (a, b) = (b, a)

for i in b:
    l =list(i)
    l.reverse()
    print(str(l))


