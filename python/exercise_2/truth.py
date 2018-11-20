x = []

if x:
    print(x, " is true")

#results:
#x = 1 is true, 22.1 is true, "hello" is true, [1,2] is true
#x = 0 or 0.0 gives no response
#x = none , x = False also no response
#x = "", [], {}, () give no response. 0 and empty lists are not considered true

#append with
x = []

if x:
    print(x, " is true")
elif not x:
    print(x, " is not recognised as true") 


