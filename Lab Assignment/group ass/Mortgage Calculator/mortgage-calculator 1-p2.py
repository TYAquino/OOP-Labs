"""
Members: Robert Hansen, Trisha Aquino and Kaleb Berhane 
Course: Object Oriented Programming 1 (CPRG-216-G)
File: 
Version: Nov. 3, 2023
"""

# Define the variables
purch_price = 0
down_payment_percentage = 0
down_payment_amount = 0
insurance_rate = 0
insurance_cost = 0
principal_amount = 0
# minimum_d_pay = 0

# Ask the user for their inputs
client_name = str(input("Enter client name: "))
address = str(input("Enter address of property: "))
purch_price = float(input("Enter purchase price: "))
down_payment_percentage = int(input("Enter the down payment percentage: "))

# Kaleb added user input minimum_d_pay
# Kaleb - We should make the purch "purchase so it's more descriptive"
# Kaleb added the calculations for the down payment

# Calculate the minimum down payment component
if purch_price <= 500000:
    if down_payment_percentage >= 5:
        print(f'{down_payment_percentage}' + '%')
    else:
        print("Please enter a minimum of 5" + "%" " for the down payment") 
elif purch_price <= 1000000:
        if down_payment_percentage >= 5:
            down_payment_amount = (down_payment_percentage/100 * 500000) + (0.10 * 300000)
            down_payment_percentage = (down_payment_amount/purch_price*100)
            print(f'{down_payment_percentage: .3f}'+ '%')
        else:
            print("Please enter a minimum of 5" + "%" + " for the down payment")    
else: 
        if down_payment_percentage >= 20:
            print(down_payment_percentage)
        else:
            print("Please enter a minimum of 20" + "%" + " for the down payment")   
    

# Ask the user for their down payment percentage


# down_payment_percentage = float(input('Enter down payment percentage (minimum {}): '))

# Calculate the mortgage default insurance component
if down_payment_percentage >= 5 < 10:
    down_payment_amount = purch_price * down_payment_percentage / 100
    insurance_cost = (purch_price - down_payment_amount) * 0.04
    principal_amount = purch_price - down_payment_amount + insurance_cost

elif down_payment_percentage >= 10 < 15:
    down_payment_amount = purch_price * down_payment_percentage / 100
    insurance_cost = (purch_price - down_payment_amount) * 0.031
    principal_amount = purch_price - down_payment_amount + insurance_cost

elif down_payment_percentage >= 15 < 20:
    down_payment_amount = purch_price * down_payment_percentage / 100
    insurance_cost = (purch_price - down_payment_amount) * 0.028
    principal_amount = purch_price - down_payment_amount + insurance_cost

else:
    down_payment_amount = purch_price * down_payment_percentage / 100
    principal_amount = purch_price - down_payment_amount + insurance_cost


# Mortgage payment component
interest_rate = 0
mortgage_term = int(input("Enter your Mortgage term from the options below \n 1, 2, 3, 5, 10: "))
while mortgage_term != [1, 2, 3, 4, 5, 10]:
    mortgage_term = int(input(("Please enter a term from the selection ")))
match mortgage_term:
      case 1:
        interest_rate = 0.0595
      case 2:
        interest_rate = 0.059
      case 3:
        interest_rate = 0.056
      case 5:
        interest_rate = 0.0529
      case 10:
          interest_rate = 0.06
#case other:
# print("Please enter a term from the selection")

amortization_period = int(input("Enter your Amortization Period from the options below \n 5, 10, 15, 20, 25: "))
while amortization_period != [5, 10, 15, 20, 25,]:
    amortization_period = int(input("Please enter a valid term from the selection: "))
total_monthly_payments = amortization_period * 12

monthly_rate = round((((((1 + interest_rate/2)**2)**0.083333) - 1)), 9)
monthly_payment = round((purch_price*(monthly_rate*((1 + monthly_rate)**total_monthly_payments))) / (((1 + monthly_rate)**total_monthly_payments)-1), 2)

print(interest_rate)
print(total_monthly_payments)
print(monthly_rate)
print(monthly_payment)          
    


# part 2
months = range(12)
opening_balance = purch_price
monthly_interest = opening_balance * monthly_rate
monthly_principle = monthly_payment - monthly_interest
closing_balance = opening_balance - monthly_principle


print(opening_balance)
print(monthly_interest)
print(monthly_principle)
print(closing_balance)

