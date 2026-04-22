data = [1, 2, 2, 3, 3, 3, "apple", "apple", "orange"]

# Initialize an empty dictionary
frequency = {}

# Loop through the list
for item in data:
    if item in frequency:
        frequency[item] += 1  # Increment if already in dict
    else:
        frequency[item] = 1   # Initialize to 1 if first time seen

print(frequency)