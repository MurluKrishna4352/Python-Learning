# count of negative and positive numbers

numbers_list_input = int(input("how_many_numbers_do_you_want_in_the_list: "))
positive = 0
negative = 0
list = []
#looping for entering element
for user in range (1 , numbers_list_input + 1):
     user_input = int(input("enter_element: " + str(user) +  ": "))
     list.append(user_input)

for i in list:
     if  (i >= 0):
           positive += 1
     else:
            negative += 1

print("positive_numbers: " , positive)
print("negative_numbers: " , negative)
