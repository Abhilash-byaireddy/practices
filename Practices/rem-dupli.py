input_string = input("Enter a string: ")
result_list = []
for char in input_string:
    if char not in result_list:
        result_list.append(char)

# Manually join characters to form the final string
final_string = ""
for char in result_list:
    final_string += char

print(final_string)
