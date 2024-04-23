class A():
    a = 21

class B():
    b = 30

class C(A,B):
    pass

c = C()

print(c.a, c.b)