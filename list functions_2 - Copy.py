# list functions
# programs

# making a different list for numbers which are divisible by 3 and are even 
even = [ i for i in range(1 , 21) if i % 3 == 0 and i % 2 == 0]
print(even)

# moving the digits in clockwise mannner

list_1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
reversing_list = [len(list_1) - 1 ] + list_1 [: [len(list_1) - 1]]
print(reversing_list)
