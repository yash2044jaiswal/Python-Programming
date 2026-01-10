# loopes in python:loops are used to repeat instructions
#while loop:
#syntax:
# while(condition):
    #statement

# #wap to print hello 50 times using while loop
# i=0
# while(i<50):
#     print("hello yash")
#     i += 1
#     #i=i+1


# #wap to print sum of numbers from 1 to 10
# i=1
# sum=0
# while(i<=10):
#     sum=sum+i
#     i += 1
# print(sum)


# #wap to print sum of digit 
# num=int(input("enter any number:"))
# sum=0
# while(num>0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)    



#wap to print reverse of digit
# rev=0
# num=int(input("enter any numnber:"))
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num //= 10
# print(rev) 
 
# other logic for printing reverse of digit
# num=int(input("enter a number:"))
# while num>0:
#     print(num%10,end=" ")
#     num=num//10



# #wap to check number is palindrom or not
# rev=0
# num=int(input("enter any numnber:"))
# orignal_num=num
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num //= 10
# if(orignal_num==rev):
#     print("number is palindrom")
# else:
#     print("number is not palindrom number")
       


#break and contineu statment:
#break statement example:
# i=1
# while(i<=5):
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("end of loop")

#continue statment example:
# i=0
# while(i<=5):
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1



#wap to print odd number 1 to 10 by using contineue keyword
# i=1
# while(i<=10):
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#practice question:
#wap to print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# #wap to print numbers from 100 to 1 reverse
# i=100
# while(i>=1):
#     print(i)
#     i-=1

#wap to print the multiplication table of a number n
# i=1
# num=int(input("enter a number:"))
# while(i<=10):
#     tab=num*i
#     print(tab)
#     i+=1


# #wap to print the elements of the following list using a loop
# list1=[]
# i=1
# while(i<=10):
#     list1.append(i**2)
#     i+=1
    
# print(list1)   




# #wap to search for a number x in this follwing tuples
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # x=int(input("enter the elements which search in tupels"))
# tup=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# x=int(input("enter number what do you wnt search"))
# i=tup
# if(x in tup):
#     print(x)
# else:
#     print("invailed input")   no solved