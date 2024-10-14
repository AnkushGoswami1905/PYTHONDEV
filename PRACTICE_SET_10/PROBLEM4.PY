# Add a static method in problem 2, to greet the user with hello.
import math
class calculator:
    
    @staticmethod   # decorator to mark greet as a static method  
    def greet(): 
        print("Hello user")

    def __init__(self,n) -> None:
        self.n=n
    def square(self):
        print(f"Square of given number is-{self.n*self.n}")
    def cube(self):
        print(f"Cube of given number is-{self.n*self.n*self.n}")
    def square_root(self):
        print(f"Square root of given number is-{math.sqrt(self.n)}") 

# Input value
v=float(input("Input value-"))
Value=calculator(v)
# Call methods
Value.square()
Value.cube()
Value.square_root()
