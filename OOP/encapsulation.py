#encapsulation of an object in python

class Employee:
    def __init__(self,id, department, age):
        self._id = id
        self._department = department
        self._age = age

    def print_data(self):
        print('id:', self._id, 'department:', self._department, 'age:', self._age)


emp1 = Employee(1233, 'Kitchen', 32)


print('Data of employee1:')

emp1.print_data()