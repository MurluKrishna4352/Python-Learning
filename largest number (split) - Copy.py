# to find largest number
a,b,c =  input("insert three numbers seperated by commas: ").split(",")
if (float(a)>= float(b)) and (float(a)>= float(c)):
    largest = a
elif (float(b)>= float(c)) and (float(b)>= float(a)):
    largest = b
else:
    largest = c


print("largest number is :", largest)    
