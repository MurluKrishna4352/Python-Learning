# def p[alindrome



def palindrome_check(word):
    if  word == word[::-1]:
        return  1
    else:
        return  0
    

input_sentence = input("Provide a sentence to the system for checking palindrome   :    ").strip().split(" ")
count = 0
print(input_sentence)

for i in input_sentence:
    if palindrome_check(i)==1:
        print("palindrome" , i)
        count += 1
        
print("Number of palindromes :   ", count)



