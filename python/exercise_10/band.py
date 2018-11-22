band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}
number=0
for i in band:
    if i in counts:
        counts[i] += 1
    else: 
        counts[i] = 1

print(str(counts)) 
