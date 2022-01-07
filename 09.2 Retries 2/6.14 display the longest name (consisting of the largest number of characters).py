arson = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = arson[0]
for i in range(len(arson)):
    if len(arson[i]) >= len(longest):
        longest = arson[i]

print("longest name:", longest)