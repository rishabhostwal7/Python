fob = open('sensor.txt', 'r')
myList = fob.readlines()

print(myList[2])
myList[2] = "This is updated third line\n"
print(myList[2])
fob.close()

fob = open('sensor.txt', 'w')
fob.writelines(myList)
fob.close()

print("Now data updation saved successfully")