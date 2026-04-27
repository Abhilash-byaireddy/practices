# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Inverting the dictionary
inverted_dict = {value: key for key, value in my_dict.items()}

# Result
print(inverted_dict)
# Output: {1: 'a', 2: 'b', 3: 'c'}
