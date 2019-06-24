import shelve
phbook = shelve.open("StudentRegister")

phbook["R001"] = {"first":"Rishabh", "last":"Ostwal", "phone":"9998887776"}
phbook["R002"] = {"first":"Stephan", "last":"Burns", "phone":"8745"}
phbook["R003"] = {"first":"Eve", "last":"Naomi", "phone":"9069"}
phbook["R004"] = {"first":"Stephen", "last":"Hawkins", "phone":"9999"}

phbook.close()

print("Student details saved successfully in shelve.")
