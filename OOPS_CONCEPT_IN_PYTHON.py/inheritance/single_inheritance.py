class A:
    def show(self):
        print("inside in class A")
class B(A):
    def display(self):
        print("inside in class B inherit with class A")
b=B()
b.display()
b.show()
# jb hm A class ka object bna kr b ke function ko access krna chahe to it is not pasible(jaise niche try kiya diya gya hai)
# a=A()
# a.display() 