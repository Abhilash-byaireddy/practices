# This program calculates the simple interest based on the principal amount, rate of interest and time in years.

p=int(input("enter the principal amount: "))
r=int(input("enter the rate of interest: "))
t=int(input("enter the time in years: "))
si=(p*r*t)/100
print(f"the simple interest is: {si}")