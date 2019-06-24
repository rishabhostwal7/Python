#List
'''
a = list()   #Used to make empty Array
print(a)

b = []        #Used to make empty Array
print(b)

#although the array is empty but all the functions related to it will be available like append(), index() etc..

a.append("Hello")
a.append(43)
print(a)

b.insert(1,33)
b.insert(4,45)
print(b)
'''
myList = list(range(1,11))
print(myList, type(myList)) # this is expanded view

myList = range(1,11)
print(myList)   # this is compact view

