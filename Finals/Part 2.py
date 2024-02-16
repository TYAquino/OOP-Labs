# import csv

# def show_appt_by_name():
#     client_name = input('Enter client name: ')
#     with open('appointments1.csv', 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         for row in reader:
#             if client_name == row[0]:
#                 print(row)
#             else:
#                 return 'No appointments found.'


def show_appt_by_name():
    client_name = input('Enter client name: ')
    matching_rows = []
    with open('appointments1.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if client_name == row[0]:
                matching_rows.append(row)
    if not matching_rows:
        return 'No appointments found.'
    else:
        for row in matching_rows:
            print(row)

# def show_appt_by_day():
#     weekday = input('Enter day of week:  ')
#     with open('appointments1.csv', 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         matching_rows = []
#         for row in reader:
#             date = str(row[1])
#             if weekday in appoinment:
#                 matching_rows.append(row)
#         return matching_rows
# matching_rows = show_appt_by_day()
# if matching_rows:
#     for row in matching_rows:
#         print(row)
# else:
#     print()

def show_appt_by_day():
    weekday = input('Enter day of week: ')
    with open('appointments1.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        matching_rows = []
        for row in reader:
            date = str(row[1])
            appointment_date = datetime.strptime(date, '%Y-%m-%d')
            if weekday == appointment_date.strftime('%A'):
                matching_rows.append(row)
        if not matching_rows:
            return 'No appointments found.'
        else:
            return matching_rows
matching_rows = show_appt_by_day()
if isinstance(matching_rows, list):
    for row in matching_rows:
        print(row)
else:
    print(matching_rows)


def find_appt_by_time():
    with open('appointments1.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        matching_rows = [row for row in reader if weekday in row[2]]
    return matching_rows
appointments = find_appt_by_time()
if appointments:
    for appointment in appointments:
        print(f"{appointment[0]} {'':^7} {appointment[1]} {'':^7} {appointment[2]}")
