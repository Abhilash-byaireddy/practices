# Declare a variable
#message = "Hell"

# Print the variable
#print(message)


#if len(message) > 5:
 #   print("Message is longer than 5 characters")



rows=5
for i in range(1,rows+1):
    for j in range(i):
        print("|",end=" ")
    print()


for i in range(rows,0,-1):
    for j in range(i):
        print("|",end=" ")
    print()


for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


n=int(input("enter a number:"))
if n>1:
     for i in range(2,n):
         if n%i==0:
            print("not prime")
            break
     else:
            print("prime")


a,b=0,1
print(a,b)