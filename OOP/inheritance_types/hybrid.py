'''
Hybrid inheritance is a blend
of more than one type of inheritance,
for instance: Multilevel and multiple
'''

class A:
    i = 5
    def say_hi(self):
        print('inside class A')

class B:
    i = 10
    def say_hi(self):
        print('inside class B')

#multiple
class C(B, A):
    i = 15
    def say_hi(self):
        print('Inside class C')

#multilevel
class D(C,B):
    def multilevel(self):
        print('The value of i on C is:', self.i)
        print('The value of i on B is:', B.i)

# Instantiate objects
c = C()
d = D()

# Call methods
c.say_hi()  # Output: inside class A
d.say_hi()  # Output: inside class A
d.multilevel()