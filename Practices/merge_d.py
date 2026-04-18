dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dict2 into dict1
merged_dict = dict1 | dict2

print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}