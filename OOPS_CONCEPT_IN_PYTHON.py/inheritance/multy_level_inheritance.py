class A:
    def disp(self):
        print("I am inside class A")
class B(A):
    def display(self):
        print("i am inside  class B with inherit class A")
class C(B):
    def show(self):
        print("i am inside class C with inherit class B")
obj1=A()
obj1.disp()
# hm class A ke object se kevla class A ka function hi access kr skte hai class B aur class C ke function ko nhi

obj2=B()
obj2.disp()
obj2.display()
# hm class B ke object se kevla class A ka function aur class B ka function hi access kr skte hai class C ke function ko nhi
obj3=C()
obj3.disp()
obj3.display()
obj3.show()
# hm class C ke object se kevla class A ka function , class B ka function aur class C ko bhi access kr skte hai 
