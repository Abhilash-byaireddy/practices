# Sample list of numbers
numbers = [10, 20, 4, 45, 99, 99, 45]

# Initialize both values to a very small number
# Using negative infinity ensures it works with any numeric input
largest = second_largest = float('-inf')

for num in numbers:
    # If the current number is greater than the current 'largest'
    if num > largest:
        # Update second_largest to the old largest, then update largest
        second_largest = largest
        largest = num
    # If current number is between largest and second_largest
    # Also ensures we don't count the same 'largest' value twice if duplicates exist
    elif num > second_largest and num != largest:
        second_largest = num

# Result Output
if second_largest == float('-inf'):
    print("There is no second largest element.")
else:
    print("The second largest element is:", second_largest)
