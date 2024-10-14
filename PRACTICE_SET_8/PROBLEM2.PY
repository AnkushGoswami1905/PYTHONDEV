# Write a python program using function to convert Celsius to Fahrenheit. 
# F = (C X 9/5)+32

def CtoF():
    c=float(input("celcius: "))
    f=((c * (9/5)) + (32))
    return f

print(f"Fahrenheit: {round(CtoF(),2)}")
