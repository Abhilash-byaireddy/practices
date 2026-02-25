"""
x=input("enter a number:")
y=x[::-1]
print(y)


n=input("enter any value:")
count=0
for i in n:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels in the string are:",count)


if x==y:
    print(x,'is palindrome')
else:
    print(x,"is not palindrome")



a=int(input("enter a value:"))
total=0
while a:
    total+=a%10
    a=a//10
print(total)


# Finding factors of a number

nums=int(input("Enter a number: "))
result=[]
for i in range(1,nums+1):
    if nums%i==0:
        result.append(i)
print(result)

#removing duplicates from list

nums=list(map(int,input("Enter a number: ")))
result=[]
for n in nums:
    if n not in result:
        result.append(n)
print(result)
"""


text=input("enter a string:")
f={}
for i in text:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(i,f)

for c in f:
    print(c,f[c])

