# define function
# def():

number_1 = float(input("provide the system with a number_1 :     "))
number_2 = float(input("provide the system with a number_2 :     "))
number_3 = float(input("provide the system with a number_3 :     "))

def  larger_number(a, b):
    if (a > b):
        return a
    return b

def  largest_number(x , y , z):
        return (larger_number(x , larger_number(y,z)))

print(largest_number(number_1, number_2, number_3))
    
