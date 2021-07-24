#patterns
# squuare pattern using "#

user_input = int(input("number_of_rows: "))

for loop in range (user_input):
     for symbol in range(4):
          print("#",end = " ")
     print()


# star ascending pattern

no_of_rows  = int(input("enter_no._of_rows: "))

for row in range(no_of_rows ):
     for coloumn in range(row + 1):
          print("*", end = "")
     print()

# number  pattern in ascending

no_of_rows  = int(input("enter_no._of_rows: "))

for row in range(1 , no_of_rows + 1):
     for column in range(1 , row + 1):
          print(column , end = " ")
     print()

     
# stars descending pattern

no_of_rows  = int(input("enter_no._of_rows: "))
for row in range(no_of_rows , 0 , -1):   # here " -1" is inserted because the star patern should go in descending ....[start : stop : step]]
     for coloumn in range (row):   # here if we insert 0 and the code mentioned here would show the same result as it takes 0 as default .
            print("*",end = " ")
     print()
             
# same numbers pattern
no_of_rows  = int(input("enter_no._of_rows: "))
for row in range (no_of_rows , 0 , -1):
     for column in range(0 , row):
          print(row , end = "")
     print()

# string  pattern  # doubt 
input_user_string = input("provide_a_word_for pattern: ")
no_of_rows = len(input_user_string)
for row in range(no_of_rows , 0 , -1):
     for coloumn in range(row):
          print(row , end ="")
     print()

# string  pattern  # doubt_2
input_user_string = input("provide_a_word_for pattern: ")
no_of_rows = len(input_user_string)
for row in range(no_of_rows , 0 , -1):
     for coloumn in range(row):
          print(no_of_rows , end ="")
     print()

# string  pattern  
input_user_string = input("provide_a_word_for pattern: ")
no_of_rows = len(input_user_string)
for row in range(no_of_rows , 0 , -1):
     for coloumn in range(row):
          print( no_of_rows , end ="")
     print()




