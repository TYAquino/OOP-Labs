"""
Members: Robert Hansen, Trisha Aquino and Kaleb Berhane 
Course: Object Oriented Programming 1 (CPRG-216-G) Final Project
File: Jojo's hair Salon.py
Program: This program asks user various questions like name and date and creates an appointment
            it also updates a csv file and creates a new one if needed. 
Version: Dec. 10,2023
"""

import os
import csv
from appointment import Appointment

def load_appointments_from_file(filename):
    appointments = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            appointment = Appointment(row[3], int(row[4]), row[0], (row[1]), int(row[2]))
            appointments.append(appointment)
    return appointments

def save_appointments_to_file(filename, appointments):
    if filename is not None:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for appointment in appointments:
                writer.writerow([appointment.get_client_name(), appointment.get_client_phone(), appointment.get_appt_type(),
                                appointment.get_day_of_week(), appointment.get_start_time_hour()])
    else:
        print("No filename provided. Appointments not saved.")

def create_weekly_calendar_file(filename):
    # Create a new weekly calendar file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Client Name", "Client Phone", "Appointment Type", "Day of Week", "Start Time"])

def main():
    filename = "weekly_calendar.csv"
    print("Starting the Appointment Manager System")
    
    create_weekly_calendar_file(filename)
    appointments = []
    # load a previous appointment schedule
    load_previous_schedule = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").lower()
    if load_previous_schedule == 'y':
        while True:
            filename = input("Enter appointment filename: ")
            if os.path.exists(filename):
                appointments = load_appointments_from_file(filename)
                print(f"{len(appointments)} previously scheduled appointments have been loaded")
                print("Jojo's Hair Salon Appointment Manager")
                print('='*37)
                print_menu(appointments, filename)
                break
            else:
                print("File not found. Re-enter appointment filename.")
        print_menu(appointments, filename)
    else:
        print("Jojo's Hair Salon Appointment Manager")
        print('='*37)
        print_menu(appointments, filename)

def print_menu(appointments, filename):
    selection = 0
    while selection != 9:
        print('1) Schedule an appointment', '\n2) Find appointment by name', '\n3) Print calendar for a specific day',
              '\n4) Cancel an appointment', '\n9) Exit the system')
        selection = int(input('Enter your selection:  '))

        match selection:
            case 1:
                schedule_appointment(appointments, filename)
                print("Jojo's Hair Salon Appointment Manager")
                print('='*37)
                print_menu(appointments, filename)
            case 2:
                find_appointment_by_name(appointments)
                print("Jojo's Hair Salon Appointment Manager")
                print('='*37)
                print_menu(appointments, filename)
            case 3:
                print_calendar_for_day(appointments)
                print("Jojo's Hair Salon Appointment Manager")
                print('='*37)
                print_menu(appointments, filename)
            case 4:
                cancel_appointment(appointments, filename)
                print("Jojo's Hair Salon Appointment Manager")
                print('='*37)
                print_menu(appointments, filename)
            case 9:
                save_scheduled_appointments(appointments, filename)
                print("Jojo's Hair Salon Appointment Manager")
                print('='*37)
                print_menu(appointments, filename)
            case _:
                input("Invalid Input \nPlease press enter to continue....")

def schedule_appointment(appointments, filename):
    print('** Schedule an appointment **')
    weekday = input('What day: ')
    start_time_hour = int(input('Enter start hour (24-hour clock): '))
    # Check if the selected day is valid
    valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    if weekday.lower() not in valid_days:
        
        print("Sorry, that time slot is not in the weekly calendar!")
        return


    # Check if the selected time slot is within the valid range
    if start_time_hour < 9 or start_time_hour >= 17:
        print("Sorry, that time slot is not in the weekly calendar!")
        return

    # Check if the selected time slot is already booked
    for appointment in appointments:
        if (
            appointment.get_day_of_week().lower() == weekday.lower()
            and appointment.get_start_time_hour() == start_time_hour
        ):
            print("Sorry, that time slot is booked already!")
            return

    client_name = input('Client name: ')
    client_phone = input('Client phone: ')
    print('Appointment types', '\n1: Mens Cut $50, 2: Ladies cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120')
    appt_type = int(input('Type of Appointment: '))

    user = Appointment('', 0, "", 0, 0)
    user.schedule(weekday, start_time_hour, client_name, client_phone, appt_type)
    appointments.append(user) 
    save_appointments_to_file(filename, appointments)  # Save to CSV
    print('Ok, ', client_name, "'s appointment is scheduled")


def find_appointment_by_name(appointments):
    print('** Find appointment by name **')
    client_name = input('Enter client name: ')
    print(f'{"Client Name"} {"":>9} {"Phone"} {"":>9} {"Day"} {"":>9} {"Start"} {"":>9} {"End"} {"":>9} {"Type"}')
    print('-'*100)

    appointments_found = False
    # Loop through the appointments and print those matching the client name
    for appointment in appointments:
        if client_name.lower() in appointment.get_client_name().lower():
            print(appointment.get_client_name(), f'{"":>9} {appointment.get_client_phone()} {"":>9} {appointment.get_day_of_week()}'
                  f'{"":>9} {appointment.get_start_time_hour()} {"":>9} {"":>9} {appointment.get_appt_type()}')
            appointments_found = True
    if not appointments_found:
        print("No appointments found.")
def show_appt_by_day(appointments, weekday):
    matching_rows = []
    for appointment in appointments:
        if appointment.get_day_of_week().lower() == weekday.lower():
            matching_rows.append(appointment)

    return matching_rows

def print_calendar_for_day(appointments):
    print('** Print calendar for a specific day **')
    weekday = input('Enter day of the week: ')
    print(f'"Client Name" "Phone" "Day" "Start" {"End":<50} {"Type":<15} ')
    print('-'*80)

    # Create a set with all available time slots for the day
    available_time_slots = set(range(9, 17))

    # Create a dictionary to store the type and client name for each available time slot
    time_slot_info = {time_slot: {'type': None, 'client_name': None, 'phone_number': None} for time_slot in available_time_slots}
    
    # Loop through the appointments and update the type and client name for booked time slots
    for appointment in show_appt_by_day(appointments, weekday):
        start_time = appointment.get_start_time_hour()
        end_time = appointment.get_end_time_hour()

        # Update the type and client name for booked time slots
        for time_slot in range(start_time, end_time):
            time_slot_info[time_slot]['type'] = appointment.get_appt_type_desc()
            time_slot_info[time_slot]['client_name'] = appointment.get_client_name()
            time_slot_info[time_slot]['phone_number'] = appointment.get_client_phone()

    # Print the available time slots along with the type and client name
    for time_slot in sorted(available_time_slots):
        type_info = f"{time_slot_info[time_slot]['type'] or 'Available':<15}"
        client_name = f"{time_slot_info[time_slot]['client_name'] or '':<20}"
        phone_number = f"{time_slot_info[time_slot]['phone_number'] or '':<15}"
        print(f"{client_name} {phone_number} {weekday.capitalize()} {time_slot:02}:00 - {(time_slot + 1):02}:00 {type_info} ")

def cancel_appointment(appointments, filename):
    print('** Cancel an appointment **')
    weekday = input('What day: ')
    start_time_hour = int(input('Enter start hour (24-hour clock): '))
    valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    if weekday.lower() not in valid_days:
        
        print("Sorry, that time slot is not in the weekly calendar!")
        return
    # checks if time hour is valid
    if start_time_hour < 9 or start_time_hour >= 17:
        print("Sorry, that time slot is not in the weekly calendar!")
        return
    # Find the appointment to cancel
    appointment_to_cancel = None
    for appointment in appointments:
        if (
            appointment.get_day_of_week().lower() == weekday.lower()
            and appointment.get_start_time_hour() == start_time_hour
        ):
            appointment_to_cancel = appointment
            break

    if appointment_to_cancel:
        # Display the cancellation details
        client_name = appointment_to_cancel.get_client_name()
        end_time_hour = appointment_to_cancel.get_end_time_hour()
        print(f'Appointment: {weekday.capitalize()} {start_time_hour}:00 - {end_time_hour}:00 for {client_name} has been canceled!')

        # Remove the appointment from the list
        appointments.remove(appointment_to_cancel)

        # Save the updated appointments to the file
        save_appointments_to_file(filename, appointments)
    else:
        print('No appointment found to cancel')

def save_scheduled_appointments(appointments, filename):
    print('** Exit the system **')
    option_save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").lower()
    
    if option_save == "y":
        fileName = input("Enter appointment filename: ")
        while os.path.exists(fileName):
            overwrite = input("File already exists. Do you want to overwrite it (Y/N)? ").lower()
            if overwrite == "n":
                fileName = input("Enter a different appointment filename: ")
            else:
                break  # Break the loop if the user chooses to overwrite

        if fileName is not None:
            save_appointments_to_file(fileName, appointments)
            print(f'{len(appointments)} scheduled appointments have been successfully saved')
        else:
            print("No filename provided. Appointments not saved.")
        save_appointments_to_file(fileName, appointments)
        print(f'{len(appointments)} scheduled appointments have been successfully saved')
    
    print('Good Bye!')

main()
