my_list = [1, 2, 3, 4, 5]
n = 2  # Number of positions to rotate left

# Normalize n to ensure it's within the list's range
n = n % len(my_list)

# Slice and concatenate
# Take from index n to the end, then add from the start to index n
rotated_list = my_list[n:] + my_list[:n]

print(rotated_list)  # Output: [3, 4, 5, 1, 2]