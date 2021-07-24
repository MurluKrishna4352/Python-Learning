 # functions of list 
 # if any function does't return anything we can not type it inside the print bracket
 
my_list = [1 , 2 ,  3   ,  4 , 5 , 6 ,7]

# reverse  function
my_list.reverse()
print(my_list)

# occurance of a single element
print(my_list.count(2))

# to clear a list
my_list.clear()
print(my_list)

# the list is cleared that is why we typed the list again here 

my_list = [1 , 2 ,  3   ,  4 , 5 , 6 ,7]

# to remove any element
my_list.remove(1)
print(my_list)
# if any element is not there in the list we tried to removed it from the above method it would show error !

my_list = [1 , 2 ,  3   ,  4 , 5 , 6 ,7]
# to remove  any number using index
# the difference between .pop() and .remove() is that in .pop() we give an index to remove and in .remove() we give a number or element to remove

my_list.pop(0)  # 0 = zero 
print(my_list)
# if we wouldn't have added the "my_list = [1 , 2 ,  3   ,  4 , 5 , 6 ,7]" it would have removed 2 because the 2 is at  "0 th" index because above in remove  1 was removed . 
