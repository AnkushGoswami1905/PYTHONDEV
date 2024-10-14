'''

Write a python function to print first n lines of the following pattern: 
*** 
**               
* 

'''
def reverse_pattern(n):
    if(n==0):  
      return
    print("*"*n)
    reverse_pattern(n-1)

n=int(input("Enter number: "))
reverse_pattern(n) 