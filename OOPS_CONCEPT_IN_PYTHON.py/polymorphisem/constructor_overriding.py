class A:
    def __init__(self):
        print("inside in class A")
class B(A):
    def __init__(self):
        print("inside in class B inherit with class A")
obj=A()
obj=B()