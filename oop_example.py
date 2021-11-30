first_employee = {'first_name': 'Corey', 'last_name': 'Rose','salary':80000}
second_employee = {'first_name': 'Mike', 'last_name': 'Lawson','salary':91000}
third_employee = {'first_name': 'Adam', 'last_name': 'Jones','salary':60000}

employees = [first_employee, second_employee, third_employee]

for employee in employees:
    print(employee['first_name'])

for employee in employees:
    employee['salary'] *= 1.1
    print(int(employee['salary']))