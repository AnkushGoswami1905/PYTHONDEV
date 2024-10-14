#Write a program to print multiplication table of a given number using while loop
n=int(input("Enter the number of which multiplication table you want to display:"))
i=1
while(i<11):
    print(n,"x",i,"=",n*i)
    i+=1

