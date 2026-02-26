for i in range(1,21):
    print(i,end=" ")
print()

for i in range(1,21):
    if i%2==0:
        print(i,end=" ")
print()

for i in range(1,21):
    if i%2!=0:
        print(i,end=" ")
print()


for i in range(1,11):
    print(i**2,end=" ")
print()

# Factorial

num =int(input("Enter a number: "))
r=1
for i in range(1,num+1):
    r=r*i
print(r,end=" ")


# Prime number

nums=int(input("Enter a number: "))
if nums>1:
    for i in range(2,nums):
        if nums%i==0:
            print(nums,"is not a prime number")
            break
    else:
        print(nums,"is a prime number")


# Palindrome

n=(input("Enter a number: "))
print(n[::-1])
print(len(n))



# Fibonacci sequence
n = int(input("Enter a number: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b