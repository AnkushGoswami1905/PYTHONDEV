a=int(input("Enter your age: "))

if(a%2==0):
    print("The entered age is even")

if(a>=18):
    print("You are above the consent age")
elif(a<0):
    print("you have entered a invalid age")    
else:
    print("You are below the consent age")
