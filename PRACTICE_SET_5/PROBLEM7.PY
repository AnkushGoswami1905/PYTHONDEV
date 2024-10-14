# If the names of 2 friends are same; what will happen to the program in problem 
# 6?
# Answer- it will updat the value of keys since keys should always be unique
#         there can not two keys with same name 

dic={}

language=input("Enter you fav language:")
name=input("Enter you Name:")
dic.update({name:language})

language=input("Enter you fav language:")
name=input("Enter you Name:")
dic.update({name:language})

language=input("Enter you fav language:")
name=input("Enter you Name:")
dic.update({name:language})

language=input("Enter you fav language:")
name=input("Enter you Name:")
dic.update({name:language})

print(dic)