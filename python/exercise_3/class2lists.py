#from the second class on python.
#dir() allows you to inspect the current environment. if we put an object #inside the brackets dir will tell us about it  
#list.insert(0, 19) will add 19 to the first position in the list
#dir(list) will tell us what modifications we can do with python built-ins
#suppose dir() shows a method 'insert', we can use help(list.insert) to access the docstring for this command.

l = range(0,10)
print(str(type(l)))

#we cqn use list comprehension 
s = [x**2 for x in range(10) is x**2 % 2 == 0]
print(s)

#this allows us to create a list in one line by placing the operations inside the list. This code tests even squares.

 

