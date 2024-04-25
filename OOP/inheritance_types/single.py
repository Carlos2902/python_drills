'''
This type of class enables to inherit 
properties and methods from the base class

The return method is not used in the init function, 
the init function is intented just to be the constructor of the class
'''

class Parent:
    i = 10
    def __init__(self) -> None:
        print( "Im the base class")
    

class Child(Parent):
    i = 5
    def __init__(self) -> None:
        super().__init__()

c = Child()


