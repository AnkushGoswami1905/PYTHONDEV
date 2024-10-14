# Write a program to find the greatest of four numbers entered by the user. 
a=int(input("Enter any number: "))
b=int(input("Enter any number: "))
c=int(input("Enter any number: "))
d=int(input("Enter any number: "))

if(a>b and a>c and a>d):
    print("The given number is greatest among all the other numbers",a)
elif(b>a and b>c and b>d):
    print("The given number is greatest among all the other numbers",b)
elif(c>a and c>b and c>d):
    print("The given number is greatest among all the other numbers",c)
else:
    print("The given number is greatest among all the other numbers",d)    