data = {'apple': 3, 'banana': 1, 'cherry': 2}
# Sorts the keys based on their values
sorted_dict = {k: data[k] for k in sorted(data, key=data.get)}
print(sorted_dict) # Output: {'banana': 1, 'cherry': 2, 'apple': 3}
