#Inherit allows the subclasses to inherit attributes and methods from a base class,
#allowing them to override its methods with their own attributes

class Animal:
    def speak(self):
        print('Animal speaks')

class Dog(Animal): #inherits from animal
    def speak(self): #override its own data
        print('Dog barks')

#instance the class
dog = Dog()

dog.speak()