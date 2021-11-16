names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longname = names[0]


for i in range(0,len(names)):
    if len(longname) < len(names[i]):
        longname = names[i]



print("Names:", end=" ")
for p in range(0,len(names)):
    print(names[p], end=" ")

print(f"\nLongest name: {longname}")
