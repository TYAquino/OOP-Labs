
class Appointment:
    def __init__(self, day_of_week, start_time_hour, client_name = '',client_phone = 0, appt_type = 0  ):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    # Getters
    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appt_type

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour

    def get_appt_type_desc(self):
        type_desc = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return type_desc.get(self.__appt_type, "Unknown")

    def get_end_time_hour(self):
        return self.__start_time_hour + 1

    # Setters
    
    def set_day_of_week(self, day_of_week):
        self.__day_of_week = day_of_week

    def set_start_time_hour(self, start_time_hour):
        self.__start_time_hour = start_time_hour

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def schedule(self, day_of_week, start_time_hour, client_name, client_phone, appt_type):
        self.set_day_of_week(day_of_week)
        self.set_start_time_hour(start_time_hour)
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)
        
        return 

    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0

    def format_record(self):
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}"

    def __str__(self):
        return f"{self.__client_name.ljust(20)} {self.__client_phone.ljust(15)} {self.__day_of_week.ljust(10)} {str(self.__start_time_hour).rjust(2)}:00 - {str(self.get_end_time_hour()).rjust(2)}:00     {self.get_appt_type_desc()}"

