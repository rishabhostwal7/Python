""" import pickle
fh = open("data.pkl",'wb')
cities = ['Lucknow', 'Noida', 'Delhi', 'Kanpur']
students = ['Rishabh', 'James', 'John', 'Jeet', 'Alisha']

pickle_object = (students, cities)
pickle.dump(pickle_object, fh)
fh.close()
print("All datas saved successfully.")
"""

# --------------------------------------------------------------------------------------

import pickle
# Unpickle multiple objets
fh = open("data.pkl", 'rb')
# x= pickle.load(fh)
(s, c) = pickle.load(fh)
print(s)
print("\n\n")
print(c)