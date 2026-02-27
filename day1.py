# reversing a string
n=input("enter a number:")
a = n[::-1]
print(a)

# counting the number of vowels in a string

a=input("enter any value:")
count=0
for i in a:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels in the string are:",count)

# finding the greatest of three numbers

a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
if a>b and a>c:
    print("a is the greatest number")
elif b>a and b>c:
    print("b is the greatest number")
else:
    print("c is the greatest number")

# checking if a number is palindrome or not

x=(input("enter any number:"))

y=x[::-1]
if x==y:
    print(x,"is palindrome")
else:
    print(x,"is not palindrome")

# sum of digits of a number

n=int(input("enter a number:"))
total=0
while n:
    total+=n%10
    n=n//10
print(total)

#removing duplicates from a list

nums=list(map(int,input("Enter a number: ")))
result=[]
for i in nums:
    if i not in result:
        result.append(i)
print(result)


# counting the frequency of characters in a string

text=input("enter a string:")
f={}
for i in text:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
for c in f:
    print(c,":",f[c])
    