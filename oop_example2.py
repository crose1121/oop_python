class Employee():

    def __init__(self, f_name, l_name, salary, m_name=None):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.salary = salary

    def full_name(self):
        if self.m_name is not None:
            return f"{self.f_name} {self.m_name} {self.l_name}"
        else:
            return f"{self.f_name} {self.l_name}"


new_employee1 = Employee('Corey', 'Rose', 72000, 'Tyler',)
new_employee2 = Employee('Mark', 'Adams', 100000, 'Michael',)
new_employee3 = Employee('Sarah', 'Jones', 81000, 'Adams', )
new_employee4 = Employee('Axel', 'Foley', 81000)

employees = [new_employee1, new_employee2, new_employee3, new_employee4]

# for employee in employees:
#     print(f"{employee.f_name} {employee.l_name}")

for employee in employees:
    print(f"{employee.full_name()}")