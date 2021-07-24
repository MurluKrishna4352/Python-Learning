# reverse string print
word = input("word_for_printing_it_indexvise: ")
opp_index = -1
length_of_word = len(word)

for index in range(length_of_word):
    print(word[index],word[opp_index],sep = " ")
    opp_index -= -1
