# All the compulsory variable ie empName must be before defined variables

def show(empName, phone="1234567890", city="Lucknow", company="XYZ"):
    print("\nempName=", empName, "phone = ", phone, "city=", city, "company=", company)


# Rule-1
show("Chintu")  # whenever a fun is invoked the value of 1st must be given ie to all the compulsory variables
# the values passed are sequentially stored from left to right in the definition of function

# Rule-2
show("Chintu", "999888")  # Positional Arguments (means it will fill sequentially)

# Rule-3
show(empName="Pappu", phone="877666")  # 2 Keyword Argument
show(phone="877666", empName="Pappu")
show(empName="Pappu", city="Kanpur")

# in a keyword argument values can be passed in any order


# Rule-4
show("Alisha", "9898", city="Delhi")  # Mixed Mode

# Following would be invalid
# ----------------------------------------------------------------------
'''
show()  # required Argument Missing
show(empName="Rishabh", "87875389")     # non-keyword argument
show("Rishabh", empName = "Alisha")     # duplicate value for empName 
show(name = "Alisha")   #unknown keyword
'''
