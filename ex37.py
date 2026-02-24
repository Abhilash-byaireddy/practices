nums=list(map(int,input("Enter numbers:").split()))
u=[]
for num in nums:
    if num not in u:
        u.append(num)
print("Unique numbers are:",u)