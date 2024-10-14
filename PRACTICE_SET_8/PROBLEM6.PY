# Write a python function which converts inches to cms
def inches_to_cms(inches):
    return inches*2.54

inches=int(input("Input inch:"))
cm=inches_to_cms(inches)
print(f"{inches}inch is {cm}cm")
            