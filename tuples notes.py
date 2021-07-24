# Tuples

#tuple_1 = "krishna" , 3 , 2 ,1
# >>> print("tuple_1" +  ' :   ' , tuple_1 )
# tuple_1 :    ('krishna', 3, 2, 1)
# >>> type(tuple_1)
# <class 'tuple'>


#>>> tuple_2 = (78)
#>>> type(tuple_2)
#<class 'int'>
#>>> tuple_2 = 78 ,     # how to declare a tuple with only one element in it , insert comma in after the element
#>>> type(tuple_2)
#<class 'tuple'>

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) # nested tuples
print(my_tuple)
print(type(my_tuple))

a , b , c = "tuples" , 1 , 2 
print(a)
print(b)
print(c)

print(type(a)) # string
print(type(b))# int
print(type(c))#int 

p , q , r  = ("mouse", [8, 4, 6], (1, 2, 3))

print(p)
print(q)
print(r)


n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'   string
print(n_tuple[1][1])        # 4   int


# tuples slicing

print(n_tuple[0][::-1]) # esuom
print(reversed(n_tuples))
                                                                    
