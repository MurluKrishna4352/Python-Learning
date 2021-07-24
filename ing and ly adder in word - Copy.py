# suffix if ended by ing then add ly else add ly
word = input("provide_a_word_for_magic: ")
word_to_find = input("word_to_find")
if len(word) < 3:
    print("provide_a_word_more_than_3_letters")
    
elif word[-3:] == "ing":
    print(word+"ly")

else:
    print(word+"ing")



#functions for string 
print(word.capitalize())
print(word.find(word_to_find))
