n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter numbers: ").split()))

even=0
odd=0
for num in nums:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers count:",even)
print("Odd numbers count:",odd)