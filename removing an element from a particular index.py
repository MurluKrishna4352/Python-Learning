# removing an element fr5om a particular postion

# user input
no_of_elements = int(input("how many element do you want in your list : "))

list_1 = []
indecies = []

for elements in range(no_of_elements):
     
     user_input = float(input("ENTER ELEMENT" + str(elements + 1 ) + " : "))
     list_1.append(user_input)
print(list_1 , " : here's your list.")

# from which index user wants to remove the element
no_of_indexes = int(input("how many indexes do you want to remove in your list  list : "))


for indexes in range(no_of_indexes):
     
     user_input_index = int(input("ENTER index" +str(indexes +1) + " : "))
     indecies.append(user_input_index -1) # -1 is added to it , for an instance the user enters 2 but the index is 1 so pytho will take it as index number 1 rather than taking it as index 2 
print(indecies , " : here's your index you want to remove.")
     
list_1 = [i for j , i in enumerate(list_1) if j not in indecies]
print(list_1 , "here's your list after removing element from a particular index")
