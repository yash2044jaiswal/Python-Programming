# class student:
#     collage_name="ABC college"
#     name="anonymous"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("add new student..")
# s1=student("karan",97)
# print(s1.name)
# print(s1.marks)
# print(s1.collage_name)
# s2=student("yash",58)
# print(s2.name)
# print(s2.marks)
# print(s2.collage_name)


class car:
    def __init__(self):
        self.acc=False
        self.breaak=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")
car1=car()
car1.start()
