n = input("Enter a number: ").lstrip('-')
if n.isdigit():
   print(f"{n} has {len(n)} digits")
else:
   print("Please enter a valid integer number.")