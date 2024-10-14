# Write a python function to print multiplication table of a given number. 
def multiplication(n):
    result=[]
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    
n=int(input("Enter number to print multiplication table: "))
multiplication(n)
