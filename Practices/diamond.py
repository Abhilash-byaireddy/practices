# Get the number of rows for the diamond (adjust as needed, an odd number makes a better diamond)
rows = 5 

# Upper half of the diamond
for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print stars
    for j in range(i * 2 + 1):
        print("*", end="")
    # Move to the next line
    print()

# Lower half of the diamond
for i in range(1, rows):
    # Print leading spaces
    for j in range(i):
        print(" ", end="")
    # Print stars
    for j in range((rows - i) * 2 - 1):
        print("*", end="")
    # Move to the next line
    print()
