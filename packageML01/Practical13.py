arr = ["Mary", "had", "a", "little", "lamb"]

print(enumerate(arr))

for i,j in enumerate(arr):
    print(i, " = ", type(i))

for i in enumerate(arr):
    print(i, " = ", type(i))