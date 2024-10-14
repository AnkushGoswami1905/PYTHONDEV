# Write a list comprehension to print a list which contains the multiplication table of a user entered number.
l=int(input("Enter a number: "))

table=[l*i for i in range(1,11)]
print(table)