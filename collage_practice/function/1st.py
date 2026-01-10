#function: is peice of code that perform specific task
#syntax: 
# def function_name:   #that is function definition
#     #statement
#function_name()      #that is function calling

# #function aliasing
# def disp():
#     print("hello world")
    
# show=disp()
# show  
# show  
# show

#nesting of function
# def display():
#     print("hello python")
#     def disp():
#         print("inside display inner")
#     disp()
# display()
#or
# def display():
#     print("hello python")
#     def disp():
#         print("inside display inner")
#     return disp()
# display()

#nesting and aliasing
def display():
    print("hello python")
    def disp():
        print("inside display inner")
        return disp()
data=display()
data
data
data 