# finding a perfect number in a range


    
def perfect_number(x):
    sum = 0
    for i in range(1 , x):
        remainder = x%i
        if remainder == 0:
            sum += i
    if sum == x:
        return 1
        #print(x , "is a perfect number : - ) ")
    else:
        return 0 
        #print(x , "is not a perfect number : - )")

start_range = int(input("Enter a starting  range for finding perfect numbers :     "))
end_range = int(input("Enter a ending  range for finding perfect numbers :     "))
list_perfect = []

for i in range(start_range , end_range):
    output = perfect_number(i)
    if output == 1:
        list_perfect.append(i)
print("NUMBER OF PERFECT NUMBERS   :    " , len(list_perfect))
print("PERFECT_NUMBERS    :    " , list_perfect)

