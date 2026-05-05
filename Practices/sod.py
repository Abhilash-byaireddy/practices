# The input number
num = 12345

# Recursive lambda: 
# It takes the last digit (n % 10) and adds it to the sum of the rest (n // 10)
sum_digits = lambda n: n if n < 10 else (n % 10) + sum_digits(n // 10)

# Result
print(f"The sum of digits is: {sum_digits(num)}")
