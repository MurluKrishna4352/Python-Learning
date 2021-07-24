# reversing a positive number
print("HELLO \n TODAY WE WILL REVERSE A NUMBER WHICH IS POSITIVE")

user_input = int(input("provide a number to reverse it : "))
reverse_number = 0


while user_input > 0:
    
    remainder = user_input %10
    reverse_number = (10*reverse_number)+remainder
    user_input //= 10
print(reverse_number , ": here's your number which is revered")
    
    
    
    
