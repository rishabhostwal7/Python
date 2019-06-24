d = {'A': 'Java', 'B': 'J2EE', 'C': 'Android', 'D': 'Python', 'E': 'Hadoop', 'Key': 'Value'}

print("len(d) = ", len(d))

del d['E']
print("After deletion of 'E' = ", d)

print("d['B'] = ", d['B'])

# print("d[2] = ", d[2]) #Dictionary do not support positional access.
print("len(d) = ", len(d))

print("'A' in d = ", 'A' in d)
print("'a' in d = ", 'a' in d)

print("d.keys() = ", d.keys())  # by taking out all the keys an array of 'list' is made
print("sorted(d.keys()) = ", sorted(d.keys()))
print("d.values() = ", d.values())
print("d.items() = ", d.items())    #it will make list of tuples where each pair has 2 values
