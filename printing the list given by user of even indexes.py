# start : stop : skip
user_input = int(input("how_many_elements_do_you_want_in_the_list: "))
list_1 = []
# loop
for i in range(user_input):
     user_element = list(input("enter_element: "))
     list_1.append(user_element)
print("here's your list : " , list_1)

for j in list_1[1::2]:
    print(j ,  end = " " )
