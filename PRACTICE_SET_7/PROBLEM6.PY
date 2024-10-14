# Write a program to calculate the factorial of a given number using for loop. 
n=int(input("Enter any number: "))
factorial=1
i=1
while(i<=n):
    factorial*=i
    i+=1
print("factorial of a given number: ",factorial)
  
f=int(input("Enter any number: "))
product=1
for i in range(1,f+1):
    product*=i
print("factorial of a given number: ",product)    
  