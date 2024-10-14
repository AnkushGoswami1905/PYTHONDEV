#  Write a program to print multiplication table of n using for loops in reversed order. 

n=int(input("Enter the number of which multiplication table is required: "))
for i in range(1,11):
    print(n, "x", (11-i) ,"=",(n*(11-i)))
