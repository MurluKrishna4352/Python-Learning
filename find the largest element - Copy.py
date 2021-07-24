# finding the maximum number 
numbers_list_input = int(input("how_many_numbers_do_you_want_in_the_list: "))
list = []
#looping for entering element
for user in range (1 , numbers_list_input + 1):
     user_input = int(input("enter_element: " + str(user) +  ": "))
     list.append(user_input)

max = int(list[0])
print(list)

for j in list:
   #  print(j)
     if  j  > max:
         max = j
print("largest element is: ",max)
