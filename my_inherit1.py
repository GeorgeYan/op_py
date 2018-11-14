class A(object):
    def show(self):
        print ('init A...')

class B(A):
    def show(self):
        super(B, self).show()
        print('init B...')
class C(A):
    def show(self):
        super(C, self).show()
        print('init C...')

class D(B, C):
    def show(self):
        super(D, self).show()
        print('init D...')
d = D()
d.show()
print(D.__mro__)
print(C.__mro__)
print(B.__mro__)
print(A.__mro__)
