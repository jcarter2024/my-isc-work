empty = {}
if empty == {}: 
    print ('hi')

d = {"maggie": "UK", "ronnie": "usa"}
print(dir(d))

print('d.items() gives ')
print(str(d.items()))

print('d.keys() gives ')
print(str(d.keys()))

print('d.values() gives ')
print(str(d.values()))

if str(d.get("")) == "None":
    print('The key does not exist')

#instead of annoying list above use the setdefault() term
d.setdefault('sex', 'Pat Uganda')
print(str(d.get('sex')))
    


