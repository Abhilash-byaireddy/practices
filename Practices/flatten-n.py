nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# The "flat" list comprehension
flat_list = [item for sublist in nested_list for item in sublist]

print(flat_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
