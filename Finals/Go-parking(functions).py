"""
Members: Robert Hansen, Trisha Aquino and Kaleb Berhane 
Course: Object Oriented Programming 1 (CPRG-216-G) Assignment 3
File: Parking-Functions.py
Program: A parking program that lets users register their license plate and credit card number. 
Version: Nov. 21, 2023
"""

# import modules
import os
import datetime

# Define variables 
lot_storage = 30
plates = []
cc_numbers = []
correct_password = "password"

# This function prints the selection menu
def print_menu(user_selection, user_options):
    while user_selection != 0: 
        match user_selection:
            case 1:
                register_vehicle()
            case 2:
                verify_vehicle()
            case 3:
                display_vehicles()
            case 4:
                display_charges()
            case 5:
                remove_vehicle()
            case 6: 
                clear_vehicles()
            case other:
                input("Invalid Input \nPlease press enter to continue....")

        print('*'*65)
        print("*** Welcome to Park and Go Parking Application! ***")
        print("Park from 6 PM - Midnight for a flat fee of $4.00")
        print('*'*65)        
        print("Select from the following options \n 1- Register a vehicle \n 2- Verify vehicle registration \n 3- Display registered vehicles and save them to a file \n 4- Display daily charges and save them to a file \n 5- Remove a vehicle \n 6- Clear vehicles \n 0- Exit")
        user_selection = int(input(">>> "))   
    print("Thanks and Good Bye!")
    return input("Please press enter to continue....")

# This function checks if the password is correct
def check_password():
    password = input("Enter your Password: ").lower()
    if password == correct_password:
        return True
    else:
        return False

# This function asks the user for licence plate and if not registered asks for the credit card and registers it.
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

# This function checks the plates and cc_numbers list and verifys the vehicle
def verify_vehicle():
    print("Verify your registration")
    while check_password() == False:
        print("Password is incorrect!")
        return input("Please press enter to continue....")
    license_plate = input("Enter your plate Number: ")
    if license_plate in plates:
        print(f"The vehicle with plate# {license_plate} is registered in the lot")
    else:
        print("The vehicle is NOT registered")
    return input("Please press enter to continue....")

# This function asks the user the password and displays all the license plates that has been currently registered
def display_vehicles():        
    while check_password() == False:
        print("Password is incorrect!")
        return input("Please press enter to continue....")
    from datetime import date
    with open('vehicles.txt', 'w') as file:
        file.write('License Plates:\n')
        if not plates:
            print("The parking lot is empty!")
            return input("Please press enter to continue....")
        else:
            print('A list of registered vehicles for', date.today())
            print('='*20)
            print(f'{"":>7} {"Plate"}')
            print('='*20)
            for license_plate in plates:
                file.write(f'{license_plate}\n')
                print(f'{"":^7} {license_plate}')
            print('='*20)
    return input("Please press enter to continue....")

# This function asks the user the password and displays all information (license plates, credit card numbers, charges and its total)
def display_charges():      
    total_charges = len(cc_numbers) * 4
    while check_password() == False:
        print("Password is incorrect!")
        return input("Please press enter to continue....")
    from datetime import date
    print('Daily parking summary for', date.today())
    print('='*65)
    print(f'{"":>7} {"Plate"} {"":>10} {"Credit Card"} {"":>9} {"Charge in $"}\n')
    print('='*65)
    with open('charges.txt', 'w') as file:
        file.write(f'License Plate, Credit Card, Charge:\n')
        for i in range(len(plates)):
            file.write(f'{plates[i]}, {cc_numbers[i]}, $4\n')
            license_plate = plates[i]
            credit_card = cc_numbers[i]
            print(f'{"":^7} {license_plate} {"":^14} {credit_card} {"":^15} 4')
    print('='*65)
    print(f'{"":>7} {"Total"} {"":>37} {total_charges}')
    return input("Please press enter to continue....")

#This function recieves input form teh user and checks if the input matches any on file license plates, and if it does, it removes the vehicle and associated credit card number, otherwise it states that there are no license plates regestered matching the input

def remove_vehicle():
    while check_password() == False:
        print("Password is incorrect!")
        return input("Please press enter to continue....")
    license_plate = (input("Enter a plate number: "))
    if license_plate in plates:
        i = license_plate.index(license_plate)
        del plates[i]
        del cc_numbers[i]
        print(license_plate, "is removed")
        return input("Please press enter to continue....")
    else:
        print(license_plate, "is not registered")
        return input("Please press enter to continue....")

#This function deletes the contents of the plates and cc_numbers lists and also wipes the vehicles.txt file clean
def clear_vehicles():
    while check_password() == False:
        print("Password is incorrect!")
        return input("Please press enter to continue....")
    open('vehicles.txt', 'w').close()
    plates.clear()
    cc_numbers.clear()
    if not plates:
        print("All vehicles were removed and the lot is empty")
        return input("Please press enter to continue....")
    else:
        print
    return input("Please press enter to continue....")

print('*'*65)
print("*** Welcome to Park and Go Parking Application! ***")
print("Park from 6 PM - Midnight for a flat fee of $4.00")
print('*'*65)
print("Select from the following options \n 1- Register a vehicle \n 2- Verify vehicle registration \n 3- Display registered vehicles and save them to a file \n 4- Display daily charges and save them to a file \n 5- Remove a vehicle \n 6- Clear vehicles \n 0- Exit")   
print_menu(user_selection = int(input(">>> ")), user_options = [1,2,3,4,5,6])
# Ask the user to select an option and get their input