# swaping a number
# 
user_input = int(input("How many elements do you want in your list : "))
_list_ = []
for i in range(user_input):
    user_list = input("Enter an element : ")
    _list_.append(user_list)
print("Here's you list : " , _list_)

fixed = _list_[0]
_list_[0]  = _list_[user_input - 1]
_list_[user_input - 1] = fixed
print(fixed)
    
    
