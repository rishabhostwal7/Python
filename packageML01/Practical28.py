print("-" * 70)

def display(a, *args):
    print("value of a : ", a)
    print("length of args : ", len(args))

# display() # It is error since a is compulsory so its value must be given
display(9)
display(1,2,3,4)
display(5,6)