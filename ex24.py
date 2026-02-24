n=int(input("enter a number:"))
original=n
power=len(str(n))
total=0
while n>0:
    digit=n%10
    total=total+digit**power
    n=n//10
    if total==original:
        print("armstrong number")
    else:
        print("Not armstrong number")