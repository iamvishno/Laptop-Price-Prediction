import pickle

# Open the pickle file in read mode ('rb' = read binary)
with open("model.pkl", "rb") as file:
    data = pickle.load(file)

print(data)  # This will print the contents of the pickle file
