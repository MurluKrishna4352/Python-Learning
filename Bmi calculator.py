# bmi .
height_inches = float(input("height_in_inches: "))
wieght_in_kg = float(input("provide_your_weight_in_kg: "))
height_feet = float(input("height_in_feet: "))
name = input("your_name: ")

# net inches
net_inches = float( height_inches + (height_feet*12))




# convers height to meters
height_in_meters = float(net_inches*2.54*0.01)


#calculates bmi
BMI = round(float(wieght_in_kg/height_in_meters**2),3)
print(name,"your bmi is:- ",BMI)


# whether you are under over or have perfect weight 

if BMI <= 18:
    print("as per your bmi you are under weight.")

elif BMI > 18 and BMI < 28:
    print("as per your bmi you are perfect .")
if BMI >= 28:
    print("as per your bmi you are obese.")
