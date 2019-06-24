# Object Oriented Programming

class Account:
    "Details for all account"       # It is like a comment and it is called as documentation comments. It is written only in the first line inside the class
    accCount=0  # class variables(outside of the functions inside the class) - Single copy existence ie memory contains only one copy of this variable
                # rest all the variables other then class and instance are called as local variables
                # HERE "n" and "b" are the local variables

    def __init__(self, n, b):   # Constructor
        self.name = n           # instance variable - Multi copy existence
        self.balance = b
        Account.accCount = Account.accCount + 1
        print("Constructor is working", b)

    def displaycount(self):
        print("Total Account = "% Account.accCount)

    def displayAccount(self):
        print("name : ", self.name, ", Balance : ", self.balance)


# Creating instance objects
ptr1 = Account("Pappu", 2000) # ptr1 is a reference variable of Account type of value
ptr2 = Account("Munni", 2000)
# Accessing Attributes


"""
Bundles of lines of code is called as function
Bundles of functions is called as class
first char of the name of the class can be upper case (Advise by Sir)
All the functions inside the class the first variable inside of it should be "self"
All the variables must be after self
if any variable has "self.variable" type will become global for all self ie it will be available for all the self inside the class
the variable made by using dot operator after self is called as instance variable
"__init__" is internal pre defined function it is called as "constructor" it behaves like starter function ie the flow starts from there
whenever a class variable is to be used it is used as "class_name.class_variable"

if num = 5.5 then num is a reference to a float type of value  
"""