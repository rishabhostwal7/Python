fob = open('sensor.txt', 'r')

data1 = fob.readlines()
# print(data1[ len(data1) -1 ])     # This is also correct
print(data1[-1])




