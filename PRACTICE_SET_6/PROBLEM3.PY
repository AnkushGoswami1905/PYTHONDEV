# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

English=int(input("Enter the marks:"))
Maths=int(input("Enter the marks:"))
Science=int(input("Enter the marks:"))

a=((English/100)*100)
b=((Maths/100)*100)
c=((Science/100)*100)
total_marks=(100*(a+b+c))/300

if(total_marks>=40 and a>=33 and b>=33 and c>=33):
    print("Passed,percentage=",total_marks)
else:
    print("Failed,percentage=",total_marks)



