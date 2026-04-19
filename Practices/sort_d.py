my_dict = {'banana': 3, 'apple': 5, 'cherry': 1, 'date': 9}

# 1. Get the keys into a list
keys = list(my_dict.keys())

# 2. Manual Bubble Sort to sort the keys alphabetically
n = len(keys)
for i in range(n):
    for j in range(0, n - i - 1):
        if keys[j] > keys[j + 1]:
            # Swap keys
            keys[j], keys[j + 1] = keys[j + 1], keys[j]

# 3. Create a new dictionary and insert items in the sorted order
sorted_dict = {}
for key in keys:
    sorted_dict[key] = my_dict[key]

print(sorted_dict)
