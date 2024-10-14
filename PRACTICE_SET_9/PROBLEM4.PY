# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.
word="Donkey"
with open("C:\PYTHONDEV\PRACTICE_SET_9\donkey.txt","r") as f:
    content=f.read()
content_new=content.replace(word,"#####")   

with open("C:\PYTHONDEV\PRACTICE_SET_9\donkey.txt","w") as f:
    f.write(content_new)
