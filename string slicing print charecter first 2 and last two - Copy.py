#string print from first two chacrecters and last two charecters
charecter_input = input("charecter_input: ")
length = len(charecter_input)

if length < 2:
    print("!input_a_charecter_more_than_two_letters!")
else:
    print(charecter_input[0:2]+charecter_input[-2:])
