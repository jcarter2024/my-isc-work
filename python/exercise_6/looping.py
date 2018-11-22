s = 'I love to write python'
split_s = s.split()
print(split_s)

for word in split_s:
    if word.rfind('i') != -1 or word.rfind('I') != -1:
        print('I found \'i\' in:' + word)
    else:
        print('I did not find the letter i in ' + word)
