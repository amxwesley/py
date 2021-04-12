def indexes(item):
    ints = [1, 3, 3, 5, 4, 3]
    
    indexes = [i for i in range(len(ints)) if ints[i] == item]
    print(f"Item {item} is found at index {indexes}")

indexes(4)
