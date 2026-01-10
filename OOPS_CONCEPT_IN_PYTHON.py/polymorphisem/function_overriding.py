class A:
    def show(self):
        print("inside in class A")
# inherit two class's in python
class B(A):
    def show(self):
        super().show()
        print("inside in class b")
b=B()
b.show()
b2=A()
b2.show()