# sets can't have the elements  as lists and dictionary
# list can consists of sets but sets can't contain lists
# sets doesn't print repeated elements

num_set = {0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 1 , 9}
for i in num_set:
    print(i)
num_set.remove(4)
print(num_set)
