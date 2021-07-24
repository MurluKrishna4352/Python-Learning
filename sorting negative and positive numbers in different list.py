#list with negative and positive numbers but will make a list  with positive numbers
no_of_elements = int(input("insert_number_how_many_time_do_you_want_to_enter_the_elements: "))
list  = []
list_positive = []
list_negative = []
for i in range (no_of_elements):
     user_list = int(input("enter_elements_for a list: "))
     list.append(user_list)
     if (user_list > 0):
          list_positive.append(user_list)
     if (user_list < 0):
         list_negative.append(user_list)
print("positive and negative list: " , list)
print("positive  list: " , list_positive)
print("negative list: " , list_negative)

# same program with list comprehension

no_of_elements = int(input("insert_number_how_many_time_do_you_want_to_enter_the_elements: "))
list  = []

for i in range (no_of_elements + 1):
     user_list = int(input("enter_elements_for a list: "))
     list.append(user_list)
newlist = [j for j in list  if j > 0]
print(newlist)
