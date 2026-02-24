nums=list(map(int,input("Enter numbers:").split()))
x=int(input("Enter number to count: "))
count=0
for num in nums:
    if num==x:
        count+=1
print("Count of",x,"is:",count)