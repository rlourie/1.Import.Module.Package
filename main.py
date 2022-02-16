from application.db.people import get_employees
from application.salary import calculate_salary
import datetime
import time

date_creation = datetime.datetime.today().strftime("%d-%m-%Y")
time_creation = time.strftime("%H.%M.%S")

print("Local Date: ", time_creation + " " + date_creation, "\n")

if __name__ == '__main__':
    calculate_salary()
    get_employees()
