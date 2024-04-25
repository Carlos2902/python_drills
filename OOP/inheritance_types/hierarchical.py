'''
This type of inheritance
has a common base class (Parent)
and two or more derived class (Childs)
'''

class Parent1:
    def __init__(self, parent_name):
        self.parentName = parent_name

class Child1(Parent1):
    def __init__(self, child1_name, parent_name):
        self.child1Name = child1_name

        Parent1.__init__(self, parent_name)

    def greeting_1(self):
        print("Hi my name is ", self.child1Name, "and my Parent's name is: ", self.parentName)


class Child2(Parent1):
    def __init__(self, child2_name, parent_name):
        self.child2Name = child2_name

        Parent1.__init__(self, parent_name)

    def greeting_2(self):
            print("Hi my name is ", self.child2Name, "and my Parent's name is: ", self.parentName)

freddy = Parent1('FREDDY')
jorge  =  Child1('jorge')
ana  =  Child2('ana')

jorge.greeting_1()
ana.greeting_2()