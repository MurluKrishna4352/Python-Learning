# finding factors of number give by user
user_input = int(input("provide_a_number_for_finding_factors: "))
list = []
#comprehension = [(for i in range(0 , user_input+1)) (if user_input % i == 0) ( list.append(i))]
for i in range(1 , user_input +1):
     if  (user_input % i == 0):
          print(i , "is the factor of: " , user_input)
          list.append(i)
print("here is the factor list: " , user_input , list)

