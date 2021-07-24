# changing the occurrences of the number according to the user

# input code
user_input = int(input("how_many_elements_do_you_want_in_the_list: "))
#variables
list = []
count = 0
count_match = 0
# loop
for i in range(user_input):
     user_element = int(input("enter_element: "))
     list.append(user_element)
print("here's your list : " , list)

#input
occurrences  = int(input("how_many_elements_do_you_want_to_replace: "))
element_find = int(input("which_element_do_you_want_to_replace: "))
user_replace = int(input("what_do_you_want_the_element_to_be_replaced_with: "))

for a in list:
     if (a == element_find and count_match <= occurrences - 1):
          list[count] = user_replace
          count_match += 1
     count += 1
print(list)
