a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
if (a > b and a < c) or (a > c and a < b):
    print("Output:", a)
elif (b > a and b < c) or (b > c and b < a):
    print("Output:", b)
else:
    print("Output:", c)