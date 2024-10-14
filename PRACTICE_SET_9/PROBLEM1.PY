# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.
f=open("C:\PYTHONDEV\PRACTICE_SET_9\poem.txt")
content=f.read()
if("twinkle" in content):
    print("The word 'twinkle' is present in poem.txt file")
else:
    print("The word 'twinkle' is not present in poem.txt file")    

f.close()

