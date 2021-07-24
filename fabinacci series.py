# fabinacci series
inesrt_terms_for_series = int(input("insert_number: "))
count = 1
n1 = 0
n2 = 1
sum = 1
if inesrt_terms_for_series <=0:
    print("insert_a_positive_number_or_a_non_zero_number: ")

elif inesrt_terms_for_series == 1:
    print(n2)
    

else:
    print("series: ")
    while(count<=inesrt_terms_for_series):
        n1 = n2
        n2 = sum
        sum = n1 + n2
        print(n1)
        count += 1
        
    
