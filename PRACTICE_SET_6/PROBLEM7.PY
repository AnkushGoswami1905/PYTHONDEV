# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 - 100 => Ex 
# 80 - 90 => A 
# 70 - 80 => B 
# 60 - 70  =>C 
# 50 - 60 => D 
# <50     => F 

student_name=input("Name-")
total_marks=int(input("Marks-"))
print(student_name)
if (total_marks>=90 and total_marks<=100) :
    print("Grade EX")
elif (total_marks>=80 and total_marks<=90) :
    print("Grade A")
elif (total_marks>=70 and total_marks<=80) :
    print("Grade B")
elif (total_marks>=60 and total_marks<=70) :
    print("Grade C")
elif (total_marks>=50 and total_marks<=60) :
    print("Grade D")
elif (total_marks<50) :
    print("Grade F")
else:
    print("Invalid Marks")    