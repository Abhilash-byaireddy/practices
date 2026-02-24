n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter numbers: ").split()))

smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num

largest = nums[0]


print("Output:", smallest)
