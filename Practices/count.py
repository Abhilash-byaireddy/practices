# Initial list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize counters
even_count = 0
odd_count = 0

# Iterate through the list
for num in numbers:
    # A number is even if it's divisible by 2 (remainder is 0)
    if num % 2 == 0:
        even_count += 1
    # Otherwise, it's an odd number
    else:
        odd_count += 1

# Display the results
print(f"Total Even numbers: {even_count}")
print(f"Total Odd numbers: {odd_count}")
