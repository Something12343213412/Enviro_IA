# takes in a file path and the data you want to save
def save_entity(file_path, data):
    file = open(file_path, "w")
    for b in data:
        file.write(f"{str(b)} \n")

# takes an input file and loops through each line adding it into an array casting it all to floats
def load_data(file_path):
    file = open(file_path, "r")
    return_array = []
    for b in file.readlines():
        return_array.append(float(b))
    return return_array

