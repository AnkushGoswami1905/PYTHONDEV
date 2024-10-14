#Write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if(n==0 or n==1):
        return n
    return (n * (n + 1)) // 2 
    
n=int(input("Enter any natural number: "))
print(f"sum of first n natural numbers: {sum(n)}")