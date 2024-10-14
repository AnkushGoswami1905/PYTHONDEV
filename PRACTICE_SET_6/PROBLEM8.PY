# Write a program to find out whether a given post is talking about “Harry” or not.

post=input("caption:")
Harry="Harry"
if Harry.lower() in post.lower():
    print(" post is talking about “Harry”")
else:
    print(" post is not talking about “Harry”")    