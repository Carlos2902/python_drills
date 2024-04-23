#multilevel inheritance
class Grandparent():
    g = 20

class Parent(Grandparent):
    g = 29

class Child(Parent):
    pass


new_child = Child()

print(new_child.g)