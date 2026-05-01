# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Keep a copy of original numbers for the final print
num1, num2 = a, b

# Euclidean Algorithm
while b != 0:
    temp = b
    b = a % b
    a = temp

print(f"The GCD of {num1} and {num2} is {a}")
