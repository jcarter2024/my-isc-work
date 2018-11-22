band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}
number=0
for i in band:
    number+=1
    mytuple = (i, number)
    print(len(mytuple))
    counts.update(mytuple)

print(str(counts)) 
