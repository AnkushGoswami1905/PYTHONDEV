# A spam string_0 is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

# string_0="Want to Make a lot of money? Don't miss out! Buy now and unlock your financial freedom! Subscribe this for exclusive tips and strategies! Click this link to start your journey today!"
# string_1="Wow, this post is amazing! I just found the ultimate way to improve my day. Everyone should check this out!"

# if "Make a lot of money" in string_0:
#     print("Spam detected!")
# elif "Buy now" in string_0:
#     print("Spam detected!")
# elif "Subscribe this" in string_0:
#     print("Spam detected!")
# elif "Click this" in string_0:
#     print("Spam detected!")
# else:
#     print("No spam.")

# if "Make a lot of money" in string_1:
#     print("Spam detected!")
# elif "Buy now" in string_1:
#     print("Spam detected!")
# elif "Subscribe this" in string_1:
#     print("Spam detected!")
# elif "Click this" in string_1:
#     print("Spam detected!")
# else:
#     print("No spam.")


a="Make a lot of money"
b="buy now"
c="subscribe this "
d="click this"

comment=(input("Comment:"))

if(a in comment or b in comment or c in comment or d in comment):
    print("spam Detected")
else:
    print("No spam")