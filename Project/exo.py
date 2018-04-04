class Employee:

    # Variable:
    raise_amount = 1.04
    # Var that keeps track of the number of employees
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Every instance of employee gets created in the __init__
        Employee.num_of_emps += 1

    def fullname(self):
        return 'Fullname: {} {}'.format(self.first, self.last)

    # Method that uses the variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Dunder repr:
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last, self.pay)


    # Dunder str: Display to end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

emp_3 = Employee('George', 'Hitler', 10000)
print(emp_3)
print(emp_3.__repr__())
print(emp_3.__str__())
