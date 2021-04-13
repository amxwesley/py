ints = [1, 3, 3, 5, 4, 3]

def indexes(item):
    
    indexes = [i for i in range(len(ints)) if ints[i] == item]
    print("Item {item} is found at index {indexes}")

indexes(3)
