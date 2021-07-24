#height in feet and inches and outout in cm
#volume of sphere .

height_inches = float(input("height_in_inches: "))
height_feet = float(input("height_in_feet: "))
name = input("your_name: ")
net_inches = float( height_inches + (height_feet*12))
print(name,"\'s, height in centimeters:",net_inches*2.54)
