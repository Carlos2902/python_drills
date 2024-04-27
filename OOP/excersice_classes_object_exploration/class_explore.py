class A:
   #constructor for A
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")
    #Local method alpha
   def alpha(self):
       c = self.c + 1
       return c

#showing attributes of the object A
print(dir(A))
print("Instantiating A..")
#instantiating object a over class A
a = A(1)
#calling method alpha() over object of class A
print(a.alpha())

#class definition of B
class B:
   #construtor for B
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a
#calling method alpha over object of class A
   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
#instantiating object A over class B
b = B(a)
print(a)