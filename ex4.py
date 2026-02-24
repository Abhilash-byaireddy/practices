# This program takes two numbers as input and compares them to determine which one is greater, or if they are equal.

a=int(input("enter the a number: "))
b=int(input("enter the b number: "))
if a>b:
    print("a is greater than b")
elif a==b:
    print("both the numbers are equal")
else:
    print("b is greater than a")