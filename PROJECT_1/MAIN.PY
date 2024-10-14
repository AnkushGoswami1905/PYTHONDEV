'''
SNAKE = 1
WATER = -1
GUN = 0

'''
import random
computer= random.choice([-1, 0, 1])

you_str=input("choose b/w S, W & G: ")
you_dict={"S":1, "W":-1, "G":0}
you=you_dict[you_str.upper()]

computer_rev_dic={1:"SNAKE", -1:"WATER", 0:"GUN"}
computer_str=computer_rev_dic[computer]

print(f"YOU CHOSE-{computer_rev_dic[you]}\nCOMPUTER CHOSE-{computer_str}")

if(computer == you):
    print("It's a DRAW")
else:
    # COMPUTER=1
    if(computer==1 and you==-1):
        print("YOU LOSE")  
    elif(computer==1 and you==0):
        print("YOU WON")  
    # COMPUTER=-1
    elif(computer==-1 and you==1):
        print("YOU WON")  
    elif(computer==-1 and you==0):
        print("YOU LOSE") 
    # COMPUTER=0     
    elif(computer==0 and you==-1):
        print("YOU WON")  
    elif(computer==0 and you==1):
        print("YOU LOSE")  
