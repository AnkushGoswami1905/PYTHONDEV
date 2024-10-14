#Can we have a set with 18 (int) and '18' (str) as a value in it?
#Ans is yes

s=set()

n=input("Enter the integer: ")
s.add(int(n))
n=input("Enter the string: ")
s.add(str(n))

print(s)