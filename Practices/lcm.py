# Get input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Start with the larger of the two numbers
if a > b:
    lcm = a
else:
    lcm = b

# Keep incrementing 'lcm' until it's divisible by both a and b
while True:
    if (lcm % a == 0) and (lcm % b == 0):
        print(f"The LCM of {a} and {b} is {lcm}")
        break
    lcm += 1
