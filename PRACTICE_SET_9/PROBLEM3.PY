#Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 
def multiplication_table(n):
    table = ""
    for i in range(1,11):
       table += (f"{n} x {i} = {n*i}\n")
    with open(f"C:\PYTHONDEV\PRACTICE_SET_9\MULTIPLICATION_TABELS\TABLE{n}.txt", "w") as f:
        f.write(table)
        
for i in range(2,21):  
   multiplication_table(i)



    

    





