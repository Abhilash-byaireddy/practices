"""
a=1
b=2
c=3
a,b,c=c,a,b
print(a,b,c)


x=[10,20,30]
y=str(x)
print(y)

"""

a = input("Enter numbers separated by spaces: ")
nums = []
for i in a:
    nums.append(int(i))

for j in range(len(nums)):
    if nums[j] < 0:
        print("Negative number", nums[j], "at index", j)
        break
else:
    print("No negative numbers found")


    count = 0
    for j in range(len(nums)):
        if nums[j] < 0:
            count += 1
            if count == 2:
                print("Second negative number", nums[j], "at index", j)
                break
    else:
        if count < 2:
            print("Less than 2 negative numbers found")