import pickle

some_data = ['apple', 'banana']

with open('data', 'wb') as file:
    pickle.dump(some_data, file)

with open('data', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data
