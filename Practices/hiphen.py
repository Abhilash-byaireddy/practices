# The original string with spaces
original_string = input("enter anything:")

# An empty string to store the modified result
modified_string = ""

# Iterate through each character in the original string
for char in original_string:
  # Check if the character is a space
  if char == ' ':
    # If it is a space, add a hyphen to the new string
    modified_string += '-'
  else:
    # If it is any other character, add the original character to the new string
    modified_string += char

# Print the final modified string
print("Original String: ", original_string)
print("Modified String: ", modified_string)
