# Program to count uppercase, lowercase, and digits without functions

input_string = "Hello World 123!" #
upper_count = 0
lower_count = 0
digit_count = 0

for char in input_string: #
    # Check for uppercase letters using ASCII range 'A' to 'Z'
    if 'A' <= char <= 'Z': #
        upper_count += 1
    # Check for lowercase letters using ASCII range 'a' to 'z'
    elif 'a' <= char <= 'z': #
        lower_count += 1
    # Check for digits using ASCII range '0' to '9'
    elif '0' <= char <= '9': #
        digit_count += 1

print("Original string:", input_string)
print("Uppercase characters:", upper_count)
print("Lowercase characters:", lower_count)
print("Digits:", digit_count)
