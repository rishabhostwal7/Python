# Pickle the data
'''import pickle

cities = ("Lucknow", "Noida", "Delhi", "Kanpur")
fh = open('data.pkl', 'wb')     # 'wb' means writing using pickling
pickle.dump(cities, fh)
fh.close()
print("All cities data are saved successfully in pickle.")'''

# Pickling / Serialization / Flatening
# to save the data using code we use pickling and to read it we do unpickling
# if we store the data using picklling then it is text file not binary file.
#---------------------------------------------------------------------------------------------

import pickle
# Unpickle the data

fh = open("data.pkl",'rb')
areas = pickle.load(fh)
print(type(areas), areas)
fh.close()

# Drawback of Pickle :- We cannot write more than once it will be replaced