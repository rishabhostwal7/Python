f = open('lines.txt', 'w')

for i in range(1,1112):
     f.writelines("{0:04d} This is developed @iitk\n".format(i))

f.close()