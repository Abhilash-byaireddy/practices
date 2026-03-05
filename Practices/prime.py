n=int(input("Enter a nuber:"))
a=0
if n>1:
    for i in range(2,n+1):
        if n%i==0:
            print("it is not prime")
            break
    else:
        print("the number is prime")
else:
    print("it is not prime")