# The number of terms you want
n = 10

# A recursive lambda function
# 'f' is the function itself, 'i' is the current number
fib = lambda f, i: i if i <= 1 else f(f, i - 1) + f(f, i - 2)

# Printing the sequence up to n
for x in range(n):
    print(fib(fib, x))
