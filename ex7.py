# This program takes a number as input and prints the multiplication table for that number from 1 to 10.

n=int(input("enter a number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")