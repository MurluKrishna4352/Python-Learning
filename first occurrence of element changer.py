# changing the occurrences of the number according to the user

# input code
user_input = int(input("how_many_elements_do_you_want_in_the_list: "))
list = []

# loop
for i in range(user_input):
     user_element = int(input("enter_element: "))
     list.append(user_element)
print("here's your list : " , list)

#variables
element_find = int(input("which_element_do_you_want_to_replace: "))
user_replace = int(input("what_do_you_want_the_element_to_be_replaced_with: "))
position_element = list.index(element_find)

#element  changer 
list[position_element] = user_replace
print("here's your list changed: " , list)
