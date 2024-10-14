# THE PERFECT GUESS 

import random
r=(random.randint(1,100))
g=-1
n=1
while(g != r):
    g=int(input("Guess any number"))
    if(g > r):
        print("Lower")
        n+=1
    elif(g < r):
        print("Higher")
        n+=1
    else:
       print(f"You have guessed the number {r} correctly in {n} attempts")
        