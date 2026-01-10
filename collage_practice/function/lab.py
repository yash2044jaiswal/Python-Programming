# # 1 #basic python programing
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# print("addition:",(a+b))
# print("subtraction:",(a-b))
# print("multiplication:",(a*b))
# print("division:",(a/b))



#2 #Area and circumference of a circle
# import math
# radius=float(input("enter the radius of the circle:"))
# area=math.pi *radius **2
# circumference=2*math.pi*radius
# print("Area:",area)
# print("circumference:",circumference)



#  # programming using branching statement
# # to check the number as odd or even
# num=int(input("Enter a Number:"))
# if num%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")



#4 # greatest of three Numbers
# a=int(input("Enter first Number:"))
# b=int(input("Enter second Number:"))
# c=int(input("Enter third Number:"))
# if a>b and a>c:
#     print("Greatest number is:",a)
# elif(b>a and b>c):
#     print("Greatest number is:",b)
# elif(c>a and c>b):
#     print("Greatest number is:",c)
# else:
#     print("Number are equals")



#5 # computing factorial
# num=int(input("Enter a Number:"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print("Factorial is:",factorial)



#6 # fibonaci series genration
# num=int(input("Enter The Number of terms:"))
# a,b=0,1
# count=0
# if num<=0:
#     print("Please enter a positive number.")
# elif num==1:
#     print("Fabonacci sequence")
#     print(a)
# else:
#     print("Fabonacci sequence")
#     while count<num:
#         print(a,end=" ")
#         a,b=b,a+b
#         count+=1





# 7prime number checking
# num=int(input("Enter a Number:"))
# if num<=1:
#     print(num,"is not a prime number")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             print(num,"is not prime number")
#             break
#         else:
#             print(num,"is  prime number")





#8 # computing sum of degit
# num=int(input("Enter a Number:"))
# sum=0
# while num>0:
#     digit=num%10
#     sum +=digit
#     num=num//10
# print("sum of digit:",sum)



#9 # programming using list tuppels
# sum of two list
# li1=[1,2,3,4]
# li2=[10,20,30,40]
# if len(li1)== len(li2):
#     result=[]
#     for i in range(len(li1)):
#         result.append(li1[i]+li2[i])
#     print("sum of two list:",result)
# else:
#     print("lists are not same length")



#10 # show a name age with tuppel
# person=("Alice",23)
# print("Name=",person[0])
# print("Age=",person[1])

# yeha tk ho gya


# programming using function
# # .factorial using Recurson
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# num=int(input("Enter a number:"))
# if num<0:
#     print("factorial does not exist for negative number:")
# else:
#     print(f"The factorial of{num} is {factorial(num)}")






# #12 # call by value and call by reference
# print("This is call by value:\n")
# def call_by_value(x):
#     print("inside function before change x= ",x)
#     x = x+10
#     print("inside function after change x= ",x)
# a=5
# print("before function call:a=",a)
# call_by_value(a)
# print("after function call: a=",a,"\n")
# print("This is call by reference:\n")

# def call_by_reference(list):
#     print("inside function before change:",list)
#     list.append(100)
#     print("inside function after change :",list)
# num=[1,2,3]
# print("before function call:",num)
# call_by_reference(num)
# print("after function call:",num)



# 13# adding two number with the help of function
# def add_numbers(a,b):
#     return a+b
# num1=int(input("Enter first number:"))
# num2=int(input("Enter secnd  number:"))
# result=add_numbers(num1,num2)
# print("The sum is:",result)




#14 #programing using string operation
# palindrom checking
# def palindrom(txt):
#     cleard=txt.replace(" "," ").lower()
#     return cleard == cleard[::-1]
# user_input=input("Enter a string:")
# if palindrom(user_input):
#     print("it is a palindrom")
# else:
#     print("it is not palindrom string")




# # 15programing using class
# show the area of ractangle with class

class ractangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
l=float(input("Enter Length:"))
w=float(input("Enter Width:"))
# creat an object of ractangle class
rect = ractangle(l,w)
print("Area of ractangle:",rect.area())

