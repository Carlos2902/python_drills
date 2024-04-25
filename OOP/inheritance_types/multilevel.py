'''
It should be a base class, intermediatory class
and a derived class for the multilevel.

The final class(derived class) attributes and methods from
the intermediatory class (which contains attributes and methods
of itself and the base class)
'''

class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfathername = grandfather_name


class Father(Grandfather):
    def __init__(self, father_name, grandfather_name):
        self.fathername = father_name

        #call the constructor to access grandfather
        Grandfather.__init__(self, grandfather_name)  

    

class Son(Father):
    def __init__(self, son_name, father_name, grandfather_name):
        self.sonname = son_name
    
    #call the constructor of father to access both: father and grandfather_name:
        Father.__init__(self, father_name, grandfather_name)
        
    def print_multilevel_names(self):
        print('Grandfathername is:', self.grandfathername)
        print('Father is:', self.fathername)
        print('My name is:', self.sonname)

andy = Son('Andy', 'John', 'Jones')
print("Father's name of Andy is: ", andy.fathername )
andy.print_multilevel_names()