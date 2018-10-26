class D:
    def foo(self):
        print("P3")

class A(D):
    def foo(self):
        print("P1")

class B:
    def foo(self):
        print("P2")


class C(A,B):
    def foo1(self):
        print("P4")

a = C()
a.foo()
