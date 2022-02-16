from application.db.people import get_employees
from application.salary import calculate_salary
import datetime
import time

DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")
TimeCreation = time.strftime("%H.%M.%S")

print("Local Date: ", TimeCreation + " " + DateCreation, "\n")

if __name__ == '__main__':
    calculate_salary()
    get_employees()
