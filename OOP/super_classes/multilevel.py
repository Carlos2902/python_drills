#multilevel inheritance
class Grandparent():
    g = 20

class Parent(Grandparent):
    g = 29

class Child(Parent):
    pass


new_child = Child()

print(new_child.g)

#Is Child subclass of...
print(issubclass(Child, Parent))
print(issubclass(Grandparent, Child))

#Is new_child instance of... the class Child?
print(isinstance(new_child, Child))


#SUPER()function
class Fruit():
    def __init__(self, fruit) -> None:
        print('Fruit type: ' + fruit)


class myFruit(Fruit):
    def __init__(self) -> None:
        super().__init__('Apple')
        print("i like  the apples")


apple = myFruit()

