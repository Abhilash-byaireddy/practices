list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert lists to sets and find common elements
common_elements = list(set(list1) & set(list2))

print(common_elements)  # Output: [4, 5]
