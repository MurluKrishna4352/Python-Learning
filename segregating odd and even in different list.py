# seperating odd and even in different lists
no_of_elemements = int(input("_provide_no._of_elements: "))
list = []
list_odd = []
list_even = []
for i in range(1 , no_of_elemements + 1):
    user_input = int( input("provide_an_element_" + str(i) + ": "))
    list.append(user_input)
    
for j in list:
     if  (j%2 == 1):
              list_odd.append(j)
     else:
               list_even.append(j)

print("orignal_list: " , list)
print("odd_list: " , list_odd)
print("even_list: " , list_even)

         
