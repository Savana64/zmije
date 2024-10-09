import pickle

with open("pickle.bin","rb") as file:
    data = pickle.load(file)

print(data)