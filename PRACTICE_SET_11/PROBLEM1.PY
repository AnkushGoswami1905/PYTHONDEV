# Create a class (2-D vector) and use it to create another class representing a 3-D vector. 
class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The 2-D vector is {self.i}i + {self.j}j")    
class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The 3-D vector is {self.i}i + {self.j}j + {self.k}k")       

t=twoDvector(3,4)
t.show()

v=threeDvector(6,4,5)
v.show()