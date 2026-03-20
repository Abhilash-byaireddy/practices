# Get input string from the user
user_string = input("Enter a string: ")

# Initialize counters for vowels and consonants
vowel_count = 0
consonant_count = 0

# Define a string of all vowels for easy checking (case-insensitive)
# Using casefold() makes the comparison suitable for all cases
cleaned_string = user_string.casefold()

# Iterate through each character in the cleaned string
for char in cleaned_string:
    # Check if the character is an alphabet letter
    if 'a' <= char <= 'z':
        # Check if the character is a vowel
        if char in 'aeiou':
            vowel_count += 1
        # Otherwise, it is a consonant
        else:
            consonant_count += 1
    # Other characters like spaces, numbers, or punctuation are ignored

# Print the final counts
print("Total Vowels:", vowel_count)
print("Total Consonants:", consonant_count)
