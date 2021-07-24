# claculator
repetition_calculator = int(input("how_many_times_do_you_want_to_calculate: "))

for i in range(repetition_calculator):
#inputs
     number = float(input("provide_a_number: "))
     number_2 = float(input("provide_a_number_2: " ))
     select_operation = input("select_operation(+,-,*,/): ")

 #addition
     if   (select_operation == "+" ) :
          print("here's your answer" , number+number_2)

#subtraction     
     if  (number > number_2 and select_operation ==" -") :
          print("here's your answer", number - number_2)

     if  (number_2 > number  and select_operation == "-") :
          print("here's your answer", number_2 - number)

     if  (number_2 == number  and select_operation == "-") :
          print("here's your answer", number_2 - number)

#multiplication
     if  (number_2 == number or number == number_2 and select_operation ==" *") :
          print("here's your answer", number **2)

     if  (number < number_2 and select_operation == "*") :
          print("here's your answer", number * number_2)

     if  (number > number_2 and select_operation == "*") :
          print("here's your answer", number * number_2)

#division
     if  (number > number_2 and select_operation == "/") :
          print("here's your answer", number/number_2)

     if  (number < number_2 and select_operation == "/") :
          print("here's your answer", number_2/number)

     if  (number == number_2 and select_operation == "/") :
          print("here's your answer", number_2/number)




