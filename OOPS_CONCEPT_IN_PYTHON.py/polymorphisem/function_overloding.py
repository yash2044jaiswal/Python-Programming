class Test:
    def show(self,*args):
        for ele in args:
            print(ele)
        print("_"*40)
t=Test()
t.show(10)
t.show(10,20)
t.show(10,20,30)
t.show(10,20,30,40)
