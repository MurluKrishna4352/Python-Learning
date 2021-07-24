# 1 to 100 perfect numbers product user_input = int(input("enter a number :  "))
product = 1
for j in range(1 , 101 ):
    sum = 0

    for i in range(1 , j):
        if (j % i==0):
            sum += i
    if (sum == j):
        print(j , "is a perfect number.")
        product *= j
print(product)
