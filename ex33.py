n = int(input("Enter number of elements: "))

nums=list(map(int, input("Enter numbers:").split()))
total=0
for num in nums:
    total+=num
print("Total sum is:",total)