# Take input from the user
user_string = input("Enter a string: ")

# Initialize a counter variable to 0
count = 0

# Iterate through each character in the string
for char in user_string:
    count = count + 1

# Print the final count (which is the length of the string)
print("Length of the string is:", count)
