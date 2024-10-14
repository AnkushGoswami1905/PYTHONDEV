# Write a program to filter a list of numbers which are divisible by 5.
def division5(n):
    if n%5==0:
        return True
    return False
l=[2,5,4,10,8,15,12,20,14,25,16,30]

s=list(filter(division5,l))
print(s)