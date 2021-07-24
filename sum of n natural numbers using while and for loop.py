# looping sum of n naturak numbers
user_input = int(input("provide_no._of_n_natural_numbers: "))
sum = 0
for i in range(1 , user_input + 1):
     sum +=  i 
print("here's your sum of " ,user_input," natural numbers: ", sum)

 # same program using while
user_input = int(input("provide_no._of_n_natural_numbers: "))
sum = 0
num = 1
while (num <= user_input ):
     sum += num
     num += 1
print(sum)
 
