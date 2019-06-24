''''# First Method
f = open('sensor.txt', 'r')
f.close()

# Second Method
with open('sensor.txt','r') as f:
    for line in f:
        print(line)'''

print("Price of %10s is %8.2f Rupees." % ("Apple",123.435))
print("Price of %-10s is %-8.2f Rupees." % ("Apple",123.435))

# print("This is {0:>10s} line written by {1:<20s}".format("First", "Rishabh"))     # Either this or ->

print("This is {0:>10s} line written by {1:<20s}".\
      format("First", "Rishabh"))

x=123
print("the value is {0:6d}".format(x))
print("the value is {0:06d}".format(x)) # This is called as padding fill
