# list of fabinacci series
insert_terms_for_list = int(input("insert_number: "))
count = 1
num_1 = 0
num_2 = 1
sum = 1
# determine an empty list
fabinacci_list = []

if insert_terms_for_list <= 0:
     print(input("provide_a_number_greater_than_0:  "))

elif  (insert_terms_for_list == 1):
     print("1")

else:
     print("list_in_series")
     while(count <= insert_terms_for_list):
          num_1 = num_2
          num_2 = sum
          sum = num_1 + num_2
          fabinacci_list.append(num_1)
          count += 1
print(fabinacci_list)
