# finding prime and composite in a ranage

def prime_check(x):
    factor_list = []
    for i in range(1 , x + 1):
        if  x % i == 0:
            factor_list.append(i)
    if len(factor_list) == 2:
        return 1
    else:
        return 0 
        
                     
        
inupt_range_start = int(input("Provide a number for starting  range  :    "))
inupt_range_end = int(input("Provide a number for ending  range  :    "))
count = 0

for i in range(inupt_range_start , inupt_range_end + 1):
    if prime_check(i) == 1:
        count += 1
        print("Prime number" , " :    " ,  i)

print("There are total :    " , count , "prime numbers ")



    
