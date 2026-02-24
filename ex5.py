# This program takes two numbers as input and swaps their values without using a temporary variable.

a = int(input("enter a number: "))
b = int(input("enter another number: "))

a, b = b, a

print(f"a : {a}")
print(f"b : {b}")
