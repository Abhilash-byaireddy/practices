main_string = "Hello, world!"
sub_string = "world"

is_present = False
# Outer loop iterates through each possible starting index in the main string
for i in range(len(main_string) - len(sub_string) + 1):
    # Inner loop checks if the substring matches the slice of the main string
    if main_string[i:i+len(sub_string)] == sub_string:
        is_present = True
        break # Exit the loop once a match is found

# Output the result
if is_present:
    print(f"'{sub_string}' is present in '{main_string}'")
else:
    print(f"'{sub_string}' is not present in '{main_string}'")
