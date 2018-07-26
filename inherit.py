class P:
    def foo(self):
        print("P")


class B(P):
    def foo(self):
        print("B")

a = B()
a.foo()
