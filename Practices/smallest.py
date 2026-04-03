numbers = [5, 3, 8, 2, 9, 1]

# Assume the first number is the smallest
smallest = numbers[0]

# Iterate through each number in the list
for num in numbers:
    # If the current number is smaller than our current 'smallest', update it
    if num < smallest:
        smallest = num

print("Smallest element is:", smallest)
