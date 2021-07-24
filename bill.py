# bill
##1 to 100 units – Rs. 10/unit
#100 to 200 units – Rs. 15/unit

#200 to 300 units – Rs. 20/unit
#above 300 units – Rs. 25/unit

units  = float(input("input_units_used: "))

if (units <= 100):

    bill = units * 10

elif (units <= 200): 

    bill = (100 * 10) + (units - 100) * 15


elif (units <= 300): 

    bill = (100 * 10) + (100 * 15) +(units - 200) * 20


elif (units > 300): 

    bill = (100 * 10) +  (100 * 15) +  (100 * 20) + (units - 300) * 25



print("YOUR BILL IS:",bill)  


    
