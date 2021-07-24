# merging of list according to length of 
list = []
list_1 = []
user_input  = int(input("how_many_elements_do_you_want_in_list_1: "))
user_input_2 = int(input("how_many_elements_do_you_want_in_list_2: "))

for i in range(1 , user_input + 1 ):
     no_elements = input("enter_element_"  + str(i) + ": ")
     list.append(no_elements)

print("enter element  for another list: ")

for j in range(1 , user_input_2 + 1 ):
     no_elements_2 = input("enter_element_"  + str(j) + ": ")
     list_1.append(no_elements_2)

list_merged = list + list_1
print("unsorted list" , list_merged)
list_merged.sort(key = len)
print("the sorted list is: " , list_merged)
