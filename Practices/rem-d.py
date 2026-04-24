# The original list with duplicates
my_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# Convert the list to a set to remove duplicates, 
# then convert it back to a list
unique_list = list(set(my_list))

# Output the result
print(unique_list)
