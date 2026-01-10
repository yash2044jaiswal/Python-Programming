class Test:
    def __init__(self,*args):
        for i in args:
            print(i)
        print("_"*40)
t=Test(10)
t=Test(10,20)
t=Test(10,20,30)
t=Test(10,20,30,40)