# Initial unsorted list
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

# Bubble Sort implementation using nested loops
for i in range(n):
    # Last i elements are already in place
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if numbers[j] > numbers[j + 1]:
            # Pythonic way to swap two variables
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
