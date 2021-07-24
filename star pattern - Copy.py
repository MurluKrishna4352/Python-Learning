#print star
num_stars = int(input("insert_rows: "))
for row in range(0,num_stars):
    for coloumn in range(row+1):
        print("*",end = "")
    print()


#letter pattern print

enter_something = input("provide_a_name_of_something: ")
length = len(enter_something)
for row in range(length):
    for coloumn in range(row+1):
        print(enter_something[coloumn],end = "")
    print()    
    

