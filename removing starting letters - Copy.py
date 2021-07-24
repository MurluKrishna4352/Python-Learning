# removing first  letters
user_input = int(input("how_many_elements_do_you_want: "))
charecter_remove = int(input("how_many_letters_do_you_want_to_remove: "))
list = []
new_list = []

for i in range(user_input):
     input_element = input("enter_element: ")
     list.append(input_element)

print("here's your list without removing the alphabets: " , list)

for k in list:
     new_list.append(k[charecter_remove:])
print("here's your list with removing the alphabets: " , new_list)

new_list_2 = [i for i in list if (len(i ) > 0)]
print(new_list_2)


