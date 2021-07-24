# count of same alphabets at the end and starting of word and if word is equal to length three the count will increase
list = []
count = 0
count_same = 0
user_input  = int(input("how_many_elements_do_you_want_in_list_1: "))

for i in range(1 , user_input + 1 ):
     no_elements = input("enter_element_"  + str(i) + ": ")
     list.append(no_elements)

for j in list:
     if (len(j) >= 3):
          count  += 1
     if (j[0] == j[-1]):
          count_same += 1
print("count of word which have more than 3 letters: " , count)
print("count of word having same letter at the end and starting: " , count_same)
          
