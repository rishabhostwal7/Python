# Arbitrary Argument List

'''def disp1(*arr):    # a '*' variable when created is always made inside round braces ie ()
    print("type(arr) = ", type(arr), arr)
    for num in arr:
        print(num)
    print("\n")

disp1(5,6,7,8)

disp1(2,3)
disp1()
disp1(9)

# ->  A '*' is used to make all the variables passed to it, it clubs/merge all the variables in it and it makes an array
# An array of * can be zero or more'''

# ----------------------------------------------------------------------------------

'''def disp(**arr):
    print(type(arr), arr)
    for k in arr.keys():
        print(k, " = ", arr[k])


disp(a='Android', b='Python', c='Java')
disp()'''

# ----------------------------------------------------------------------------------

def sum(*values):
    sum = 0
    for num in values:
        sum = sum+num
    print("Addition Result of %d numbers =%d" % (len(values),sum))
    return

sum(2,3,4,5)
sum(3,4,6)

# '*' makes tuples
# '**' is used to make pairs