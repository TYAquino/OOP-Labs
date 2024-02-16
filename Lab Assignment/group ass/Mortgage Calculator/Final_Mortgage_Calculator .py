"""
Members: Robert Hansen, Trisha Aquino and Kaleb Berhane 
Course: Object Oriented Programming 1 (CPRG-216-G)
File: Final-Mortgage-Calculator.py
Version: Nov. 07, 2023
Program: This program is a mortgage calculator. It calculates numbers such as monthly payment, total mortgage payment, monthly interest as well as insurance price and it does so by asking the user for various inputs, like the price of the house, the amount of down payment they want to put and the term for their mortgage.
"""


'''
Part 1 - Monthly Payment Calculator
'''
# Define the variables
purch_price = 0
down_payment_percentage = 0
down_payment_amount = 0
insurance_rate = 0
insurance_cost = 0
principal_amount = 0
term_selection = (1,2,3,5,10)
amortization_selection = (5, 10, 15, 20, 25)

# Ask the user for their inputs
client_name = str(input("Enter client name: "))
address = str(input("Enter address of property: "))
purch_price = int(input("Enter purchase price: "))

# Calculate the minimum down payment component
if purch_price <= 500000:
    minimum_d_pay = 0.05 * purch_price
    minimum = (minimum_d_pay / purch_price) * 100
elif (purch_price >= 500000) and (purch_price < 1000000):
    minimum_d_pay = 0.05 * 500000 + (purch_price - 500000) * 0.10 
    minimum = (minimum_d_pay / purch_price) * 100
else:
    minimum_d_pay = 0.20 * purch_price
    minimum = (minimum_d_pay / purch_price) * 100

down_payment_percentage = float(input(f'Enter down payment percentage (minimum {minimum: .3f}): '))
while (down_payment_percentage < minimum) or (down_payment_percentage > 100):
            print('Please enter a value between the minimum and 100')
            down_payment_percentage = float(input(f'Enter down payment percentage (minimum {minimum: .3f}): '))

# Calculate the mortgage default insurance component
if (down_payment_percentage >= 5) and (down_payment_percentage < 10):
        down_payment_amount = purch_price * down_payment_percentage / 100
        insurance_cost = (purch_price - down_payment_amount) * 0.04
        principal_amount = (purch_price - down_payment_amount) + insurance_cost

elif (down_payment_percentage >= 10) and (down_payment_percentage < 15):
        down_payment_amount = purch_price * down_payment_percentage / 100
        insurance_cost = (purch_price - down_payment_amount) * 0.031
        principal_amount = (purch_price - down_payment_amount) + insurance_cost

elif (down_payment_percentage >= 15) and (down_payment_percentage < 20):
        down_payment_amount = purch_price * down_payment_percentage / 100
        insurance_cost = (purch_price - down_payment_amount) * 0.028
        principal_amount = (purch_price - down_payment_amount) + insurance_cost

else:
        down_payment_amount = purch_price * down_payment_percentage / 100
        principal_amount = (purch_price - down_payment_amount) + insurance_cost

print(f'Down payment amount is ${down_payment_amount:.0f}')
print(f'Mortgage insurance price is ${insurance_cost:.0f}')
print(f'Total mortgage amount is ${principal_amount:.0f}')

# Ask the user for their choice of mortgage term
mortgage_term = int(input(f"Enter mortgage term {term_selection}: "))

# If the user does not select the right term the program does not continue
while not mortgage_term in term_selection:
    print("Please enter a valid choice")
    mortgage_term = int(input(f"Enter your Mortgage term {term_selection}: "))

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
    case other:
          print("Please enter a term from the selection")

amortization_period = int(input("Enter mortgage Amortization Period (5, 10, 15, 20, 25): "))
total_monthly_payments = amortization_period * 12

# If the user does not select the right amortization the program does not continue
while not amortization_period in amortization_selection:
      print("Please enter a valid choice")
      amortization_period = int(input(f"Enter mortgage Amortization period {amortization_selection}: "))
      total_monthly_payments = amortization_period * 12
      
monthly_rate = (((((1 + interest_rate/2)**2)**0.0833333333) - 1))
monthly_payment = (principal_amount*(monthly_rate*((1 + monthly_rate)**total_monthly_payments))) / (((1 + monthly_rate)**total_monthly_payments)-1)

print(f"Interest rate for the term will be {interest_rate:.2%}")
print(f"Monthly payment amount is: ${monthly_payment:.0f}")  
    

'''
Part 2 of the calculator
Displays the schedule of monthly payment if the users want to see.
'''
schedule = input("Would you like to see the amortization schedule? (Y/N): ").upper()   
total_months = mortgage_term * 12
opening_balance = (purch_price - down_payment_amount) + insurance_cost
monthly_interest = opening_balance * monthly_rate
monthly_principle = monthly_payment - monthly_interest
closing_balance = opening_balance - monthly_principle
principal_list = []
interest_list = []

# if the user selects y then the loop excecutes and upon calulating the numbers it displays them as a table
if(schedule=="Y"):
      print(f"{'':^31} {'Monthly Amortization Schedule'}\n")
      print(f"{'Month':>8} {'':^4} {'Opening Bal':>10} {'':^5} {'Payment':>10} {'':^5} {'Principal':>10} {'':^5} {'Interest':>10} {'':^4} {'Closing Bal':>10}")
      for month in range(total_months):
            principal_list.append(monthly_principle)
            interest_list.append(monthly_interest)
            print(f"{month + 1:>8} {'':^5} {opening_balance:>10.2f} {'':^5} {monthly_payment:>10.2f} {'':^5} {monthly_principle:>10.2f} {'':^5} {monthly_interest:>10.2f} {'':^5} {closing_balance:>10.2f}")
            opening_balance = closing_balance
            monthly_interest = opening_balance * monthly_rate
            monthly_principle = monthly_payment - monthly_interest
            closing_balance = opening_balance - monthly_principle

      principal_total = sum(principal_list)
      interest_total = sum(interest_list)

      print('='*95)
      print(f"{'Total'} {'':^42} {principal_total:>10.2f} {'':^5} {interest_total:>10.2f}")
