n=int(input("ente a number:"))
if n<0:
    print("prime doesn't contain negative values")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")