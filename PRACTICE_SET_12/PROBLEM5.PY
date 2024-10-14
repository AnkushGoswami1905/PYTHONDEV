# Store the multiplication tables generated in problem 3 in a file named Tables.txt
l=int(input("Enter a number: "))

table=[l*i for i in range(1,11)]
with open("Table.txt","a") as f:
    f.write(f"Table of {l}:{str(table)}\n")
