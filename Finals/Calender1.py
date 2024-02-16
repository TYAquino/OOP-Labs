def create_weekly_calender():
    weekday = (input("Enter day of the week:  ").lower)
    print("Appointments for", weekday)
    if weekday == 'monday':
        appt_list = []
        day = "Monday"
        for time in range(9, 16):
            appt_list.append(ap.Appointment(day, time))
        return
    elif weekday == 'tuesday':
        appt_list = []
        day = "Tuesday"
        for time in range(9, 16):
            appt_list.append(ap.Appointment(day, time))
        return
    elif weekday == 'wednesday':
        appt_list = []
        day = "Wednesday"
        for time in range(9, 16):
            appt_list.append(ap.Appointment(day, time))
        return
    elif weekday == 'thursday':
        appt_list = []
        day = "Thursday"
        for time in range(9, 16):
            appt_list.append(ap.Appointment(day, time))
        return
    elif weekday == 'friday':
        appt_list = []
        day = "Friday"
        for time in range(9, 16):
            appt_list.append(ap.Appointment(day, time))
        return
    elif weekday == 'saturday':
        appt_list = []
        day = "Saturday"
        for time in range(9, 16):
            appt_list.append(ap.Appointment(day, time))
        return
    elif weekday == 'sunday':
        appt_list = []
        day = "Sunday"
        for time in range(9, 16):
            appt_list.append(ap.Appointment(day, time))
        return
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    for appt in appt_list:
        print(appt)