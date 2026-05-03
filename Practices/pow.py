def power(base, exp):
    # Base case: anything to the power of 0 is 1
    if exp == 0:
        return 1
    # Recursive case: base * (base to the power of exp - 1)
    else:
        return base * power(base, exp - 1)

# Usage
print(power(2, 3)) # Output: 8
