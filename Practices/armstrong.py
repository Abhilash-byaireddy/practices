n = int(input("Enter the numbers: "))
digit = 0
power = len(str(n))
sum_of_powers = 0

for i in str(n):
    digit = int(i)
    sum_of_powers += digit ** power

if sum_of_powers == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")