#Write a program to print multiplication table of a given number using for loop.
n=int(input("Enter the number of which multiplication table you want to display:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
