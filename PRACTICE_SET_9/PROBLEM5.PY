words=["Fuck","Bitch","Asshole"]

with open("C:\PYTHONDEV\PRACTICE_SET_9\censor.txt","r") as f:
    content=f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("C:\PYTHONDEV\PRACTICE_SET_9\censor.txt","w") as f:
    f.write(content)      
