class A:
    def show(self):
        print("A class method")

class B(A):
    def show(self):
        print("B class method")

class C(A):
    def show(self):
        print("C class method")

class D(B, C):
    pass

d = D()
d.show()

print(D.__mro__)
