# sets
#sets are unordered 
# union(common) -----> | -->       operator is used
# intersection (prints what is common in between them)---------> & operator is used

set_1 = {"apple" , "mango" , "banana" , "orange" , "kiwi"}
set_2 = {"apple" , "banana" , "kiwi"}
# union
print(set_1 | set_2)

#intersection
print(set_1 & set_2)

#intersection_update

set_1.intersection_update(set_2)
print(set_1)


a = {1 , 2 , 3 }
b = {3 , 5 , 6}
c = {7 , 9 , 1}
a.intersection_update(b , c)
print(a) # would print empty set() as there is no common element between a b c

# set -----> deep copy (if set_2 is changed it would also affect set_1 which is the first set )
# = creates a deep copy  

set_2 = set_1
set_2.add(5)
print(set_2)
print(set_1)

# set -----> shallow copy (if set_2 is changed it would not  affect the set_1 which is the first set )

set_2 = set_1.copy()
set_2.add(10)
print(set_2)
print(set_1)












 
