# Take input from the user
user_input_string = input("Enter a string with spaces: ")

# Initialize an empty string to store the result
string_without_spaces = ""

# Iterate through each character in the input string
for char in user_input_string:
    # Check if the current character is not a space
    if char != ' ':
        # If it's not a space, add it to the new string using concatenation
        string_without_spaces += char

# Print the original and the modified string
print("Original string:", user_input_string)
print("String without spaces:", string_without_spaces)
