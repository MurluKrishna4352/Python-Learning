#lower alphabets
#numbers
#upper alphabets
input_for_checking = input("provide_a_word/number/mix_of_both: ")
check_upper = 0
check_lower = 0
check_digit = 0
for index in range(0,len (input_for_checking)):
    if input_for_checking[index].isupper():
        check_upper += 1
    elif input_for_checking[index].islower():
         check_lower += 1
    elif input_for_checking[index].isdigit():
        check_digit += 1
print("the word you gave have {} upper case, {} lower case, {} digits".format(check_upper,check_lower,check_digit))
    
    
