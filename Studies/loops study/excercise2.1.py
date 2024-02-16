''' program header
program: Excercise2.1.py
Author: Trisha
Description:
Version: Sep 22, 2023
'''

# Step 1 get the current price
current_price = int(input("Please enter the current price>>> "))

# Step 2 get the last month price
last_month_price = int(input("Please enter the last month price>>> "))

# Step 3 processing
change_in_prices = current_price - last_month_price
monthly_mortgage = current_price * 0.051 / 12

# Step 4 display a summary
print(f"Current Price = {current_price} \nChange in Prices ={change_in_prices} \nEstimated Mortgage = {monthly_mortgage}")