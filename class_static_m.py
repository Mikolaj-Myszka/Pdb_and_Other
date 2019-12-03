# # Python OOP
# # 1. classmethods
# class Employee:

#     num_of_emps = 0
#     raise_amt = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = (self.pay * self.raise_amt)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount


# emp_1 = Employee('Corey', 'Schafer', 5000)
# emp_2 = Employee('Test', 'Employee', 6000)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)



# 2. staticmethods
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = (self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'Employee', 6000)

import datetime

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
