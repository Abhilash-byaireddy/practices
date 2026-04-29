# Factorial using a recursive lambda
n = 5
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)

# Result
print(f"The factorial of {n} is {factorial(n)}")
