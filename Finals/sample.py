import csv

def delete_row(appointments1, row_number):
    with open('appointments1.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)

    with open('appointments1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in reader:
            if reader.line_num != row_number:
                writer.writerow(row)

with open('appointments1.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == weekday:
                    lines.remove(row)
    with open('appointments1.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(lines)

class Appointment:
    def __init__(self, title, start, end, description):
        self.title = title
        self.start = start
        self.end = end
        self.description = description
    
    def __str__(self):
        return f"{self.title}, {self.start}, {self.end}, {self.description}"
    
appointment = Appointment("Meet with John", datetime.time(10, 30), datetime.time(11, 30), "Discuss project progress")
with open("appointments.csv", "a") as csvfile:
    fieldnames = ["Title", "Start", "End", "Description"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"Title": appointment.title, "Start": appointment.start, "End": appointment.end, "Description": appointment.description})