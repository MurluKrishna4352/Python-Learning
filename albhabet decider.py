# alphabet decider
chr = input("provide_charecter: ")
asci =  ord(chr)
if (ord("A") <= asci and ord("Z")>= asci):
    print(chr+"is capital")
elif (ord("a") <= asci and ord("z")>= asci):
    print(chr ,"is small ")
else:
    print("not a chr")

if  ((chr == 'a') or (chr == 'i') or (chr == 'o') or (chr == 'e') or (chr == 'u')):
    print(chr+"is a vowel.")
else:
    print(chr,"is a consonant.")
