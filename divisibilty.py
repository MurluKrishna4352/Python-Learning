#list with negative and positive numbers but will make a list  with positive numbers
no_of_elements = int(input("insert_number_how_many_time_do_you_want_to_enter_the_elements: "))
list  = []
list_2 = []
for i in range (no_of_elements):
     user_list = int(input("enter_elements_for a list: "))
     list.append(user_list)
list.sort()

for j in list:
    if(j > 180):
        break
    if  j % 5 == 0:
       list_2.append(j)
       
print(list_2)
    
for z in list_2:
    print(z , end = " ")
