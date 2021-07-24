# pow = function
# pow(base , to the power)
# program to find compund intrest

principle_amt = float(input("Provide the amount of principle : "))
rate_interest = float(input("Provide the amount of rate of intrest : "))
time_years = float(input("Provide the amount of time in years : "))

# calculating compound interest
ci = principle_amt * (pow((1 +  rate_interest  / 100) , time_years))
print(ci , ": here's your compund interest")

