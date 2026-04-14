# 1. Take space-separated input from the user and convert to a list of integers
user_input = input("Enter your numbers separated by space: ")
nums = [int(x) for x in user_input.split()]

# 2. Identify the start and end of your range
start = min(nums)
end = max(nums)

# 3. Calculate the expected sum of a complete sequence from start to end
# Formula for sum of consecutive integers: (n / 2) * (first + last)
n = end - start + 1
expected_sum = (n * (start + end)) // 2

# 4. Calculate the actual sum of user-provided numbers
actual_sum = sum(nums)

# 5. Find the difference
missing_number = expected_sum - actual_sum

if missing_number == 0:
    print("No number is missing in the range.")
else:
    print(f"The missing number in the range {start} to {end} is: {missing_number}")
