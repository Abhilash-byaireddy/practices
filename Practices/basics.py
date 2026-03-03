#Hello world program
print("Hello world!")

#input name
name=input("Enter your name:")
print("welocme to python programming",name)

#arithmetic operations

a=10
b=5
print(a+b)

#swap the values of a and b
a,b=b,a
print("a=",a)
print("b=",b)

#power of a and b
print(a**2,a**3)
print(b**2,b**3)

#check if the number is even or odd
c=int(input("enter the numbers:"))
if c%2==0:
    print("number is even")
else:
    print("number is not even")

#check which is greater among two
d=int(input("enter the number:"))
e=int(input("enter the number:"))
if d>e:
    print("d is greater than e")
elif d<e:
    print("d is less than e")
else:    
    print("d is equal to e")

    
#check which is greater among three
f=int(input("enter the number:"))
g=int(input("enter second number:"))
h=int(input("enter third number:"))
if f>g and f>h:
    print("f is large number:")
elif g>f and g>h:
    print("h is large:")
elif h>f and h>g:
    print("h is large:")
else:
    print("all are equal")


#check if the year is leap or not
k=int(input("enter the year:"))
if (k%4==0 and k%100!=0) or (k%400==0):
    print("leap year")
else:
    print("the year is not leap")

#factorial of a number
l=int(input("enter the number:"))
r=1
for i in range(1,l+1):
    r=r*i
print(f"factorial of {l} is {r}")
