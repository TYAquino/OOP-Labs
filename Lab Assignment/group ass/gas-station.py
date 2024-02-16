"""
Members: Robert Hansen, Trisha Aquino and Kaleb Berhane 
Course: Object Oriented Programming 1 (CPRG-216-G)
Program: The program asks the user to select gas or oil. 
         After the users selection the program asks for the amount
         and the province they live and displays the appropriate prices.
Version: Oct. 15, 2023
"""

# Welcome message
print('-'*45)
print(f'{"*** Welcome to Gas Station Program! ***":<100}')
print('-'*45)

# Define variables
print("Please select the type of purchase:\nG: Gas\nO: Oil")
selection = input(">>> ").upper()
gas_amount = 0
gas_max = 0
oil_max = 0
oil_amount_cases = 0
oil_amount_liters = 0
gas_price = 0
oil_price = 0
gas_per_liter = 1.07
oil_per_liter = 1.27
gas_coupon = 0
oil_coupon = 0

# Define a condition that asks the user to select gas or oil
if((selection=="G") or (selection=="O")):
    # Calculate the gas price with coupon
    if(selection=="G"):
        gas_max = 4000
        gas_amount = int(input("Enter the number of litres of gas: "))
        gas_price = gas_amount * gas_per_liter
        if(gas_amount < gas_max):
            gas_coupon = gas_amount * gas_per_liter
        else:
            gas_coupon = gas_amount * gas_per_liter * -0.10 + gas_amount * gas_per_liter
    elif(selection=="O"):
        # calculate the oil price with coupon
        oil_max = 8
        oil_amount_cases = int(input("Enter # of cases of Oil: "))
        oil_amount_liters = oil_amount_cases * 12 
        oil_price = oil_amount_liters * oil_per_liter

        if(oil_amount_cases < oil_max):
            oil_coupon = oil_price = oil_amount_liters * oil_per_liter
        else:
            oil_coupon = oil_amount_liters * oil_per_liter * -0.10 + oil_amount_liters * oil_per_liter

    # define GST based on province choice
    province = input("Please enter the 2 letters province abbreviations: ").upper()
            
    if(province=="AB" or province=="BC" or province=="MB" or province=="NT" or province=="NU" or province=="QC" or province=="SK" or province=="YT") and (oil_amount_cases or gas_amount) <= (gas_max or oil_max):
        GST = (gas_price * 0.05) + (oil_price * 0.05)
    elif(province=="AB" or province=="BC" or province=="MB" or province=="NT" or province=="NU" or province=="QC" or province=="SK" or province=="YT") and (oil_amount_cases or gas_amount) >= (gas_max or oil_max):
        GST = (gas_coupon * 0.05) + (oil_coupon * 0.05)
    elif(province=="ON") and (gas_amount or oil_amount_cases) <= (gas_max or oil_max):
        GST = (gas_price * 0.13) + (oil_price * 0.13)
    elif(province=="ON") and (gas_amount or oil_amount_cases) >= (gas_max or oil_max):
        GST = (gas_coupon * 0.13) + (oil_coupon * 0.13)
    else:
        GST = (gas_price * 0.15) + (oil_price * 0.15)
    
    print('-'*120)
    # define total price based on oil or gas  amount
    if (gas_amount < gas_max):
        total_price = (oil_price + gas_price) + GST
    else:
        total_price = (gas_coupon + oil_coupon) + GST

    # print the results 
    if(selection=="G"):
        print(f" Product\t # Of Litres\t Price Before Discount\t Price After Discount\t  GST\t\t total Price \n Gas \t\t {gas_amount} \t\t\t {gas_price}\t\t\t{gas_coupon: .2f}\t {GST: .2f}\t {total_price}")
        print('-'*120)
        print("Thanks for your business, Good Bye")
    else:
        print(f" Product\t # Of Litres\t Price Before Discount\t Price After Discount\t  GST\t total Price\n  Oil\t\t  {oil_amount_liters}\t\t\t {oil_price}\t\t\t {oil_coupon: .2f} \t {GST: .2f}\t {total_price: .2f}")
        print('-'*120)
        print("Thanks for your business, Good Bye")

else:
    print("Invalid input, you should enter g/G or o/O")