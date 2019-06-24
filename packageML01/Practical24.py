d = {'A': 'Java', 'B': 'J2EE', 'C': 'Android', 'D': 'Python', 'E': 'Hadoop', 'Key': 'Value'}

keyList = d.keys()
for k in sorted(keyList):
    print(k, d[k])

print("Data Type = ", type(d.items()))

for key, value in d.items():
    print(key, " = ", value)

print("d['A'] = ", d['A'])
# print("d['Z'] = ", d['Z'])

print("d.get('Z') = ", d.get('Z'))
