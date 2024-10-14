#Write a program to find whether a given number is prime or not. 
n=int(input("Enter the number: "))
i=2
while(i<n-1):
    i+=1
    if(n%i)==0:
        print("NON PRIME")
        break
else:
    print("PRIME")


p=int(input("Enter the number: "))
for i in range(2,p):
    if(p%i)==0:
        print("NON PRIME")
        break
else:
    print("PRIME")
