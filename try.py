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


text=input("enter a string:")
f={}
for i in text:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
    
for c in f:
    print(c,f[c])

# Second largest number in a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number:", second)

# Missing number in a list

number=list(map(int,input("Enter numbers separated by space: ").split()))
n=len(number)+1
total=n*(n+1)//2
sum_of_numbers=sum(number)
missing=total-sum_of_numbers    
print("Missing number:", missing)

# Longest word in a sentence

sentence=input("enter a sentence:")
words=sentence.split()
longest=words[0]
for word in words:
    if len(word)>len(longest):
        longest=word
print("Longest word:", longest)


# Armstrong number
n = int(input("Enter number: "))
s = 0
t = n
d = len(str(n))

while t > 0:
    r = t % 10
    s = s + r**d
    t = t // 10

if s == n:
    print(f"{n} is Armstrong")
else:
    print(f"{n} is Not Armstrong")

# Anagrams
s1=input("Enter first string: ").lower()
s2=input("enter second string:").lower()
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")

# Count uppercase, lowercase and digits in a string

s=input("Enter a string: ")
upper=0
lower=0
digits=0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digits+=1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)  
print("Digits:", digits)


n=int(input("Enter a number: "))
total=0
for  i in range(2,101):
    if i%n==0:
        total+=i
print(total)




