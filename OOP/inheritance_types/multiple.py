'''
Multiple inheritance allows the child
to inherit from different parents

The child C by default is gonna look up
first for the class with major herarchy,
the one that was passed as a parameter first
'''

class A():
    def greeting(self):
        return "Inside class A"

class B():
    def greeting(self):
        return "Inside class B"


class C(B,A):
    pass

c = C()
print(c.greeting())
