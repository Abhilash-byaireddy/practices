n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter numbers: ").split()))

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Output:", largest)
