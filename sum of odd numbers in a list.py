# user input of how many series do they they want
# sum of odd numbers
numbers_list_input = int(input("how_many_numbers_do_you_want_in_the_list: "))
sum = 0
list = []
#loop for repeatition of input of enter element
for user in range(numbers_list_input):
   user_input = int(input("enter_element: "))
   list.append(user_input)
print(list)


for i in range(numbers_list_input ):
     if  list[i]%2  == 1:
          sum += list[i]

print(sum)
