# Write a program to find the sum of first n natural numbers using while loop. 
n=int(input("Enter any natural number: "))
natural_number=0
i=1
while(i<=n):
    natural_number+=i
    i+=1
print("Sum of first n natural nunmber:",natural_number)
    