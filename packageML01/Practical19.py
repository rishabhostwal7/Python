# Rule-1: Lists are Mutable ie it can be changed

'''a = ["Noida", "Delhi", "Lucknow", "Goa", "Kanpur"]
a[3] = "UK"
print(a)

a.append("Patna")
print(a)

del a[1]
print(a)

a.insert(2,"Varanasi")
print(a)
'''

#Rule-2: Tuple is immutable
tu = ("Python", "Java", "J2ee", "Android", "Hadoop")
print(type(tu), tu)
#tu[3] = "RDBMS"  #This line is Error

print("tu.index('Android') = ", tu.index("Android") )
print("'Hadoop' in tu = ", "Hadoop" in tu)
print("'Crysta' in tu = ", "Crysta" in tu)
