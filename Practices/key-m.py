data = {'apple': 15, 'banana': 42, 'cherry': 28}

# Initialize with None or a very small number
max_key = None
max_val = -float('inf') 

for key in data:
    if data[key] > max_val:
        max_val = data[key]
        max_key = key

print(max_key)  # Output: banana
