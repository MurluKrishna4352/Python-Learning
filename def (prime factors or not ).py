# finding the prime number using define function



def  prime_check(number):

    
    count = 0

    for i in range(1 , number + 1):
        remainder = number % i
        if remainder == 0:
            count+=1
    if count == 2:
        return True
    return False

starting_range = int(input("Provide a starting range :       "))
ending_range =  int(input("Provide an ending range :       "))

def count_prime(starting_range , ending_range):
    count_prime_no = 0
    

    for j in range(starting_range , ending_range + 1 ):

        if(prime_check(j)):
            count_prime_no += 1


    return count_prime_no

print("Number of prime  numbers :     ",count_prime(starting_range , ending_range))


def sum_prime(starting_range , ending_range):
    sum_prime_no = 0

    for k in range (starting_range , ending_range + 1 ):
        if (prime_check(k)):
            sum_prime_no += k

    return sum_prime_no
print("Sum of the prime numbers is :   ",sum_prime(starting_range , ending_range))
