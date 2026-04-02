# Sample list
numbers = [12, 45, 7, 23, 99, 54]

# Step 1: Assume the first element is the largest
largest = numbers[0]

# Step 2: Loop through the list to compare elements
for n in numbers:
    if n > largest:
        largest = n

# Step 3: Print the result
print("The largest element is:", largest)
