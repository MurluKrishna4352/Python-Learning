# changing the occurrences of the number according to the user

# input code
user_input = int(input("how_many_elements_do_you_want_in_the_list: "))
list = []
# loop
for i in range(user_input):
     user_element = int(input("enter_element: "))
     list.append(user_element)
print("here's your list : " , list)

element_remove = int(input("provide_an_element_to_remove: "))
index_find = list.index(element_remove)

comprehension = [ z for z in range if (z == element_remove)]
print(comprehension , list.remove(index_find))

