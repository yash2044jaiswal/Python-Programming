class A:
    def info(self):
        print("i am inside class A")
class B(A):
    def show(self):
        print("i am class B inherit with class A")
class C(B):
    def show1(self):
        print("i am class C inherit with class B")
class D(B):
    def disp(self):
        print("i am class C inherit with class B")
class E(C,D):
    def disp1(self):
        print("i am class E inherit with class C and D")
obj1=A()
obj1.info()
# obj1.show()# not accessble
obj2=B()
obj2.info()
obj2.show()
obj3=C()
obj3.info()
obj3.show()
obj3.show1()
obj4=D()
obj4.disp()
obj=E()

