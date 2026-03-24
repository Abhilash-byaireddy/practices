input_string = "Hello, world!"
frequency_dict = {}

# Iterate through each character in the string
for char in input_string:
    # Check if the character is already in the dictionary
    if char in frequency_dict:
        # If yes, increment its count
        frequency_dict[char] += 1
    else:
        # If no, add it with a count of 1
        frequency_dict[char] = 1

# Print the character code (character) and its frequency
print("Character Code (Character) : Frequency")
for char_code in frequency_dict:
    print(char_code, ':', frequency_dict[char_code])
