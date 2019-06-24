arr = ["Mary", "had", "a", "little", "lamb"]

print(enumerate(arr))

for i,j in enumerate(arr):
    print(i, " = ", j)

# Will be divided like this internally
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb