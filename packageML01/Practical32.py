# File handling in Python

fob = open('sensor.txt', 'w')
abc = fob.write("This is first line")   # no. of char which are written successfully in a file is stored in variable abc
print("Result = ", abc)
fob.close()
print('Data saved Successfully')


# while opening any file if no mode is given then by default it is taken as 'Read Mode'
#------------------------------------------------------------------------------------------------

fob = open('sensor.txt','r')
print(fob.read(6))
print("Latest starting location = ", fob.tell())
print(fob.read())
print("First : ", fob.closed)   # fob.closed will tell whether the file is been closed or not
fob.close()
print("Second : ", fob.closed)  # it is a boolean variable