# file ModuleTwo.py
import ModuleOne    # when this line is executed then all the lines inside the ModuleOne will be executed
                    # this line is writen to connect ModuleOne with ModuleTwo

print("top - level in ModuleTwo.py")
print("ModuleTwo :__name__ = ", __name__)
ModuleOne.func()

if __name__ == "__main__":      # it is similar to psvm in java
    print("ModuleTwo.py is being run directly")
else:
    print("ModuleTwo.py is being imported into another module")


# Every file contains internal variable whose name is  "__name__"