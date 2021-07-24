# odd and even using define
def odd_even(number):
     if (number % 2 == 0):
          print(number , " : is even.")
     else:
          print(number , " : is odd.")

number = int(input("provide_a_number_to_chech_its_odd_or_even: "))
odd_even(number)
