# adding the cubes of the same number like 45 add 4 cube + 5 cube
# 783//10  -> 78 {floor operator }
# if the sum of the cubes of the digits of the numbers is equal to the number itself called armstrong numbers
# % ----->  used for finding the remainder .

user_input = int(input("provide_a_number : "))
sum = 0
temp = user_input 

while temp > 0:
     digit = temp % 10
     sum += digit ** 3
     temp //= 10
print(sum , ": sum of the cubes of the numbers of the digits")

if (sum == user_input):
      print(user_input , ": is an ARMSTRONG NUMBER" )
else:
     print(user_input , ": is not an ARMSTRONG NUMBER")

