n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter numbers: ").split()))

print("reversed list:", nums[::-1])