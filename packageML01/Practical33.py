fob = open('sensor.txt', 'r')
print('Data1 = ', fob.readline())
print('Data2 = ', fob.readlines())
fob.close()

# readline() readlines() are used for reading a file lin.e by line