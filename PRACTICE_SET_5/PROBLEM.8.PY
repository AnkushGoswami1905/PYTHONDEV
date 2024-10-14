# If languages of two friends are same; what will happen to the program in problem 
# 6? 
# Answer-if the values(language)are same of two different keys(friends) it will show keys with same 
#        value since two keys can have same values, only the key name should be unique

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