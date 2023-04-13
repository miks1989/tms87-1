class A_1:
    pass
class A0(A_1):
    pass
class A(A0):
    pass

class B:
    pass

class C(B):
    pass

class D(A, C):
    pass

print(D.mro())