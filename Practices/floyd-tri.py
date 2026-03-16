# Prompt user for the number of rows
rows = int(input("Enter the number of rows: "))
# Initialize a variable to keep track of the number to be printed
number = 1

print("Floyd's Triangle:")

# Outer loop controls the number of rows
for i in range(1, rows + 1):
    # Inner loop controls the number of elements in each row
    # The number of elements in each row is equal to the current row number (i)
    for j in range(1, i + 1):
        # Print the current number followed by a space (to stay on the same line)
        print(number, end=' ')
        # Increment the number for the next iteration
        number += 1
    # Print a newline character after each row to move to the next line
    print()
