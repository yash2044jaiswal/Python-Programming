# Encapsulation:-binding data member and member function into sigle slight
class Bank:
    __name=None
    __acc_no=None
    __balance=None
    def __init__(self,name,acc_no,balance=0):
        self.__name=name
        self.__acc_no=acc_no
        self.__balance=balance
    def profileDeltailes(self):
        print("Account holder name:",self.__name)
        print("Account Number :",self.__acc_no)
        print("Balance:",self.__balance)
        print("_"*50)
    def deposite(self,amount):
        if amount>0:
            self.__balance +=amount
            
            print("Deposite Amount:",amount)
            print("Deposite Successfully..")
            print("update Balence :",self.__balance)
            print("_"*50)
        else:
            print("invailed Ammount...")
            print("_"*50)
    def withdraw(self,amount):
        if amount > 0 and amount< self.__balance:
            self.__balance -=amount
            print("withdraw ammount:",amount)
            print("withdraw successfully...")
            print("update Balence :",self.__balance)
            print("_"*50)
        else:
            print("invailed ammount..")
            print("_"*50)

user1=Bank("yash",389456,5000)
user1.profileDeltailes()
user1.deposite(1000)
user1.profileDeltailes()
user1.withdraw(2000)
user1.profileDeltailes()
user2=Bank("Harsh",389456,2000)
user2.profileDeltailes()
user2.deposite(1000)
user2.profileDeltailes()
user2.withdraw(2000)
user2.profileDeltailes()