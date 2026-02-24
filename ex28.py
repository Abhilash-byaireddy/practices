a=input("enter a string:")
s=""
for i in a:
    if i.lower() not in "aeiou":
        s=s+i
print("output:",s)