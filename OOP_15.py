class A:
    def show(self):
        print("A ka show()")

class B(A):
    def show(self):
        print("B ka show()")

class C(A):
    def show(self):
        print("C ka show()")

class D(B, C):
    pass

d_obj = D()
d_obj.show()

print(D.__mro__)