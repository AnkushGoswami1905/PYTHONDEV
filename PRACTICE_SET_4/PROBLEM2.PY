#Write a program to accept marks of 6 students and display them in a sorted manner.
MARKS=[]

f1=int(input("Enter MARKS here- "))
MARKS.append(f1)
f2=int(input("Enter MARKS here- "))
MARKS.append(f2)
f3=int(input("Enter MARKS here- "))
MARKS.append(f3)
f4=int(input("Enter MARKS here- "))
MARKS.append(f4)
f5=int(input("Enter MARKS here- "))
MARKS.append(f5)
f6=int(input("Enter MARKS here- "))
MARKS.append(f6)
f7=int(input("Enter MARKS here- "))
MARKS.append(f7)

MARKS.sort()

print(MARKS)
print(type(MARKS))