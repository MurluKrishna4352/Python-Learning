# armstrong def

def armstrong_check(num):
    temp_num = num
    sum = 0
    length = len(str(num))
    while temp_num > 0:
        digit_num = temp_num % 10
        sum += digit_num ** length
        temp_num = temp_num // 10
    if sum == num:
        return 1
    else:
        return 0

input_start = int(input("Enter a number :     "))
input_end = int(input("Enter a number :     "))
count = 0
armstrong = []
sum = 0

for i in range(input_start , input_end + 1):
    if  armstrong_check(i) == 1:
        count += 1
        armstrong.append(i)
        sum += i
print(count , "count")
print(sum , "sum")
print(armstrong , "    :  armstrong numbers   ")


    

    
    
