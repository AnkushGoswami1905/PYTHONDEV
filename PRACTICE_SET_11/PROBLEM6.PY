# Write __str__() method to print the vector as follows: 
# 7i + 8j +10k 
class vector:

    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v=vector(7,8,10)    
print(v)