# The following example uses more complex values for

'''import shelve

products = shelve.open("MyProducts.txt")
products['P001'] = "Mouse"
products['P002'] = "Keyboard"
products['P003'] = "Monitor"
products['P004'] = "Printer"
products['P005'] = "DVD"
products['P003'] = "Music System"
products.close()
print("All the products data saved in shelve")
'''

# Using shelve we can treat a file just like dictionary
# ------------------------------------------------------------------------------------
import shelve
products = shelve.open("MyProducts.txt")

for pid in products:
    print(pid, " = ", products[pid])

print("All product details printed from file.")