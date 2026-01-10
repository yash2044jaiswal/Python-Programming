# polymorphisem:
# inbuild function for arithmatic function in python
# + -> __add__(self,other)
# - -> __sub__(self,other)
# / -> __div__(self,other)
# * -> __mul__(self,other)
# ** -> __pow__(self,other)
# // -> __flotdiv__(self,other)
# += -> __iadd__(self,other)
# -= -> __isub__(self,other)
# /= -> __idiv__(self,other)
# *+ -> __imul__(self,other)

# for relational operator
# > -> __gt__(self,other)
# < -> __lt__(self,other)
# >= -> __ge__(self,other)
# <= -> __le__(self,other)
# == -> __eq__(self,other)
# != -> __ne__(self,other)



class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(100)
b2=Book(200)
print("total no of pages:",b1+b2)



# class Employee:
#     def __init__(self,salery):
#         self.salery=salery
#     def __mul__(self,other):
#         return self.salery * other.days
# class Timesheet:
#     def __init__(self,days):
#         self.days=days
# emp=Employee(2000)
# ts=Timesheet(30)
# print("month:",emp*ts)