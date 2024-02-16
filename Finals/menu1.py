import csv

def print_menu():
   print('1) Schedule an appointment', '\n2) Find appointment by name', '\n3) Print calender for a specific day', '\n4) Cancel an appointment', '\n9) Exit the system')
   selection = input('Enter your selection:  ')
   if selection == 1:
    print('** Schedule an appoinment **')
    weekday = input('What day: ')
    start_time_hour = input('Enter start hour (24 hour clock) : ')
    client_name = input('Client name: ')
    client_phone = input('Client phone: ')
    print('Appointment types', '\n1: Mens Cut $50, 2: Ladies cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120')
    appt_type = input('Type of appointment: ')
    #add getters/setters code here
    print('Ok, ', client_name,"'s appointment is scheduled")
    return
   elif selection == 2:
    print('** Find appointment by name **')
    client_name = input('Enter client name: ')
    print('Appointments for ', client_name)
    #add find_appointment_by_name() function here
    return

   elif selection == 3:
    print('** Print calender for a specific day **')
    weekday = input('Enter day of week:  ')
    print('Appointments for', weekday)
    print(create_weekly_calender.weekday)
    return
   elif selection == 4:
    print('** Cancel an appointment **')
    weekday = input('What day: ')
    start_time_hour = input('Enter start hour (24 hour clock :) ')
    #enter cancel() code here
    return
   elif selection == 9:
    print('** Exit the system **')
    #add save_scheduled_appointments() code here
    return
   else: None     


