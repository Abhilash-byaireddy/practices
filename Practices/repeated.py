s = input("Enter a string: ")
freq = {}

# Count occurrences
for char in s:
    freq[char] = freq.get(char, 0) + 1

# Find the character with the maximum count
max_char = max(freq, key=freq.get)
print(f"Most repeated character: {max_char}")
