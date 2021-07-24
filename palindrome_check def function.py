# def p[alindrome



def palindrome_check(word):
    if  word == word[::-1]:
        return 1
    else:
        return 0

input_list_no= int(input("Enter number of elements you want in your list  :    "))
list_1 = []
for i in range(input_list_no + 1):
    list_elements = input("Enter element" , str(i + 1)  , " :  ")
    list_1.append(list_elements)
print(list_1)    
print(palindrome_check(list_1))
