class A:
    def c(self):
        return "Function inside A"
    

class B(A):
    def c(self):
        return "Function inside B"
    

class C(A,B):
    pass


class D(C):
    pass

d = D()
print(d.a)