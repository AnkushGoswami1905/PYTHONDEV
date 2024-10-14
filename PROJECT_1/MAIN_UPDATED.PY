import random
computer= random.choice([-1, 0, 1])

you_str=input("choose b/w S, W & G: ")
you_dict={"S":1, "W":-1, "G":0}
you=you_dict[you_str.upper()]

computer_rev_dic={1:"SNAKE", -1:"WATER", 0:"GUN"}
computer_str=computer_rev_dic[computer]

print(f"YOU CHOSE-{computer_rev_dic[you]}\nCOMPUTER CHOSE-{computer_str}")

#The below logic is written on the basis of the value of computer - you
if(computer == you):
    print("It's a DRAW")   
elif((computer - you) == -1 or  (computer - you) == 2 ):
        print("You lose!")
else:
        print("You won!")
