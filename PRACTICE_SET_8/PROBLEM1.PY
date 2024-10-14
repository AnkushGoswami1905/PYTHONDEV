# Write a program using functions to find greatest of three numbers.
def greatest():
    a=(int(input("Enter number 1: ")))
    b=(int(input("Enter number 2: ")))
    c=(int(input("Enter number 3: ")))

    if(a>b and a>c):
        print(f"Number 1 is greatest {a}")
    elif(b>a and b>c):
        print(f"Number 2 is greatest {b}")
    else:
        print(f"Number 3 is greatest {c}") 

def maximum(A,B,C):
    if(A>B and A>C):
        return A
    elif(B>A and B>C):
        return B
    else:
        return C 
       
A=(int(input("Enter number A: ")))
B=(int(input("Enter number B: ")))
C=(int(input("Enter number C: ")))
print(f"Greatest: {maximum(A,B,C)}")

# greatest()
  