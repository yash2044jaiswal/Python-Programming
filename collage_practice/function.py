# #Function in python
# def disp():
#     print("hello!Good Morning")
# disp()   
# disp()

#Function with parameter
# def display(name):
#     print(f"hello {name} good morning")
# display("ajay")
# display("yash")    

# # #Function with parameter
# def display(name,dname):
#     print("hello" ,name,  "good morning" ,dname)
# display("ajay","jal")



# #write a function to take number as input and print its sqare value
# def square(number):
#     print(f"the square of {number} is {number * number}")
# square(5)
# square(4)    



# #return statement
# #Function can take input values as parameters and executes business logic and return
# #write a function to accept two number as input and return sum
# def add(x,y):
#     return x+y
# result=add(10,20)
# print(f"sum={result}")
# print(f"sum={add(100,200)}")
# #if we are not writing return statmentthen default returnvalue is none.



# #write a function to check wheather the given number is even or odd
# def even_odd(num):
#     if num%2==0:
#         print(f" {num} is even number")
#     else:
#         print(f"{num} is odd number")
# even_odd(10)
# even_odd(15)


#write  a function to print factorial of a gin=ven number




# # 17.#wap to print sum of degit
# def sumofdigit(num):
#     add=0
#     while(num>0):
#         rem=num%10
#         add=add+rem
#         num=num//10
#     print("sum of digit:",add)
# number=int(input("Enter a number:"))
# sumofdigit(number) 


# recursion
# def fun(num):
#     if(num==1):
#         return 1
#     else:
#         return num*fun(num-1)
# print(fun(5))

# decorator
# def decorator(func):
#     def wrapper(name):
#         print("good morning")
#         func(name)
#         print("thanks for calling me")
#         return name
#     return wrapper
# @decorator
# def greet(name):
#     print("hii",name)
# greet("rakesh")


# lambda /anonomous function
# wap to print square of number by using lambda function
# squar=lambda num:num*num
# print(squar(5))

# #wap to adding two number by using lambda function
# add=lambda a,b:a+b
# print(add(3,4))




# # decorator

# def decor(addition):
#     def inner():
#         th=addition()
#         et=int(input("enter anumber:"))
#         et=et+th
#         return et
#     return inner
# def addition():
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     c=int(input("enter a number:"))
#     sum=a+b+c
#     return sum
# add=decor(addition)
# print(add())