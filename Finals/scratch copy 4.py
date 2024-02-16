"""
Members: Robert Hansen, Trisha Aquino and Kaleb Berhane 
Course: Object Oriented Programming 1 (CPRG-216-G)
File:
Program:
Version: Nov. 21, 2023
"""

import os
import datetime


lot_storage = 30
plates = []
# total_charges = charge + charge 
cc_numbers = []
correct_password = "password"
def print_menu(user_selection, user_options):
    while user_selection != 0: 
        match user_selection:
            case 1:
                register_vehicle()
            case 2:
                verify_vehicle()
            case 3:
                display_vehicles()
            # Trish your code goes here
            case 4:
                display_charges()
            # Also Trisha's code
            case 5:
                while check_password() == False:
                    print("Please Enter the correct password")
                
            # Robert your code goes here
            case 6: 
                while check_password() == False:
                    print("Please Enter the correct password")
                
            # Also Robert's code
            case other:
                input("Invalid Input \nPlease press enter to continue....")
                
        print("Select from the following options \n 1- Register a vehicle \n 2- Verify vehicle registration \n 3- Display registered vehicles and save them to a file \n 4- Display daily charges and save them to a file \n 5- Remove a vehicle \n 6- Clear vehicles \n 0- Exit")
        user_selection = int(input(">>> "))   
    print("Exit")

def check_password():
    password = input("Enter your Password: ").lower()
    if password == correct_password:
        return True
    else:
        return False

# Kaleb's function
def register_vehicle():
    if lot_storage < 50:
        print("The parking lot has spaces for your vehicle")
        license_plate = input("Enter your plate Number: ")
        if license_plate not in plates:
            credit_card = input("Enter your Credit Card Number ($4:00 charge): ")
            plates.append(license_plate)
            cc_numbers.append(credit_card)  
            print(f"Thank you, your plate {license_plate} has been added to the lot.")
        else:
            print(f"{license_plate} is already registered")
    else:
        print("The parking lot is full")
    return input("Please press enter to continue....")


# Kaleb's function
def verify_vehicle():
    print("Verify your registration")
    while check_password() == False:
        print("Password is incorrect!")
        input("Please press enter to continue....")
    license_plate = input("Enter your plate Number: ")
    if license_plate in plates:
        print(f"The vehicle with plate# {license_plate} is registered in the lot")
    else:
        print("The vehicle is NOT registered")
    return input("Please press enter to continue....")

        
# Trisha's function
def display_vehicles():
    while check_password() == False:
        print("Password is incorrect!")
    with open('vehicles.txt', 'w') as file:
        file.write('License Plates:\n')
        from datetime import date
        print('A list of registered vehicles for', date.today())
        print('='*20)
        print(f'{"":>7} {"Plate"}')
        print('='*20)
        for license_plate in plates:
            file.write(f'{license_plate}\n')
            print(f'{"":^7} {license_plate}')
        print('='*20)
    return input("Please press enter to continue....")


# Trisha's function
def display_charges():
    # total_charges = 0
    # total_charges = len(cc_numbers) * 4
    while check_password() == False:
        print("Password is incorrect!")
    with open('charges.txt', 'w') as file:
        # file.write(f'License Plate, Credit Card, Charge:\n')
        # from datetime import date
        # print('Daily parking summary for', date.today())
        # print('='*65)
        # print(f'{"":>7} {"Plate"} {"":>10} {"Credit Card"} {"":>9} {"Charge in $"}\n')
        # print('='*65)
        for i in range(len(plates)):
            file.write(f'License Plate: {plates[i]}, Credit Card: {cc_numbers[i]}, Charge: $4\n')
            license_plate = plates[i]
            credit_card = cc_numbers[i]
            print(f'{"":^7} {license_plate} {"":^10} {credit_card} {"":^12} $4')
    print('='*65)
    print(f'{"":>7} {"Total"} {"":>37} ')
    # print(f'{"":>7} {"Total"} {"":>37} ${total_charges}')
    # return input("Please press enter to continue....")

# Robert's function
def remove_vehicle():
    return remove_vehicle

# Robert's function
def clear_vehicles():
    return clear_vehicles

# Define variables 

# lot_storage = 30
# plates = []
# # total_charges = charge + charge 
# cc_numbers = [""]
# correct_password = "password"

print('*'*65)
print("*** Welcome to Park and Go Parking Application! ***")
print("Park from 6 PM - Midnight for a flat fee of $4.00")
print('*'*65)
print("Select from the following options \n 1- Register a vehicle \n 2- Verify vehicle registration \n 3- Display registered vehicles and save them to a file \n 4- Display daily charges and save them to a file \n 5- Remove a vehicle \n 6- Clear vehicles \n 0- Exit")   
print_menu(user_selection = int(input(">>> ")), user_options = [1,2,3,4,5,6])


# Ask the user to select an option and get their input



# print(f'This is the list of cars registered {plates}')
# print(f'This is the list of credit cards{cc_numbers}')


