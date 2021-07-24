# string 1 string 2 = swaping of first letters
string_1 = input("provide_a_word: ")
string_2 = input("provide_a_word_2: ")
swap_letters = string_2[:2] + string_1[2:]
swap_2_letters = string_1[:2] + string_2[2:]
print(swap_letters,swap_2_letters,end = " ")
