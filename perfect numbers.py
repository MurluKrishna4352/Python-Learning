# perfect number ----> is a number in which the sum of factors of the the number is equal to the number 
user_input = int(input("enter a number :  "))
sum = 0

for i in range(1 , user_input):
    if (user_input % i==0):
        sum += i
if (sum == user_input):
    print(user_input , "is a perfect number.")
else:
    print(user_input , "is a not perfect number.")
    
        
