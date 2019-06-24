'''
def show(*arr):
    print("No of element in array = ", len(arr))
    print("Data type of arr = ", type(arr))
    print(arr)


show(1, 2, 3, 4, 5)  # values will be packed
print("\n")

list1 = [1, 2, 3, 4, 5]
show(list1)  # values will be unpacked

print()
show(*list1)  # values will be unpacked here and then it is packed

print()
tuple1 = (1, 2, 3, 4, 5)
show(tuple1)  # values will be packed
show(*tuple1)  # values will be unpacked

# -> To merge all the values into one array is called as packing of values, in this case = *arr
# -> * can be used of packing as well as unpacking
'''


# --------------------------------------------------------------------------------------
# Unpacking Arguments List

print(list(range(3, 6)))

args = [3, 6]
print(list(range(args[0], args[1])))

print(list(range(*args)))
