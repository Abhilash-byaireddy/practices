list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Convert lists to sets and find the intersection
common = set(list1) & set(list2)

if common:
    print("Common elements found:", list(common))
else:
    print("No common elements.")
