rows = 5 # You can change this number for a different number of rows

# Outer loop to handle the number of rows
for i in range(1, rows + 1):
    # Inner loop to print leading spaces for alignment
    for j in range(rows - i):
        print(" ", end="")
        
    # Inner loop to print the numbers in the first half of the pyramid
    for k in range(1, i + 1):
        print(k, end="")
        
    # Inner loop to print the numbers in the second half of the pyramid (decreasing sequence)
    for l in range(i - 1, 0, -1):
        print(l, end="")
        
    # Move to the next line after each row
    print()
