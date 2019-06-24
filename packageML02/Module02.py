# connecting with math lirary
import math                         # External Import or External Linking
print(math.sqrt(25))
print(math.pi)

# Adding all features of math library
# in the program
from math import *                  # Internal Import or Internal Linking
print(sqrt(16))
print(pi)

# Adding selective features of math
# library in the program
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Nick name to the linked library
import math as chintu               # External Import
print(chintu.sqrt(25))
print(chintu.pi)

import Module01
Module01.show(4)
Module01.sum(2, 3)
print(Module01.count)

from packageML02 import Module01
Module01.show(7)
Module01.sum(3, 5)
print("Module01.count = ", Module01.count)


from packageML02.Module01 import *
show(3)

show(6)
sum(2, 3)
print(count)
