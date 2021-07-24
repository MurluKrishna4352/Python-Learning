 # def function
# calculator
print("HELLO WORLD !!!\n\n")
print("-----> Enter + for addition\n")
print("-----> Enter  -  for subtraction\n")
print("-----> Enter  *  for multiplication\n")
print("-----> Enter  /  for division\n")
#inputs 


# addition function 
def sum(x , y):
    if (input_condition == "+"):
        return x + y
# subtraction function 
def subtraction( x , y ):
    if (input_condition == "-"):
        return x - y
# multiplication function 
def multiplication(x , y):
    if (input_condition == "*"):
        return x * y
# division function 
def division(x , y):
    if (input_condition == "/"):
        return x / y
    
while True :
    number_1 = float(input("Provide the system with first number :     "))
    number_2 = float(input("Provide the system with the second number :     "))
    input_condition = input("Enter the condition :    ")
    if (input_condition == "+"):
         print(number_1 , input_condition , number_2 , " =  ", sum(number_1 , number_2))
    elif (input_condition == "-"):
         print(number_1 , input_condition , number_2 , " =  ", subtraction(number_1 , number_2))
    elif (input_condition =="*"):
         print(number_1 , input_condition , number_2 , " =  ", multiplication(number_1 , number_2))
    elif (input_condition == "/"):
         print(number_1 , input_condition , number_2 , " =  ", division(number_1 , number_2))
    else:
        print("Invalid Input \n Try Again : - ) ")
        print("Enter yes to quit and sustain to continue .")
        sustainment = input("do yo want to quit ?   :     ")
        if sustainment == "yes":
            break
        else:
            continue
