sentence = input("enter anything: ")
longest_word = ""
current_word = ""

for char in sentence:
    if char != " ":
        current_word += char
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""

# Check the last word in the sentence as it won't have a space after it
if len(current_word) > len(longest_word):
    longest_word = current_word

print("The longest word is:", longest_word)
