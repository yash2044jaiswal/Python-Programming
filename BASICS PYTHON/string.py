# string 's function

# str="yash"
# print(str[0])#y
# # this is method use for print the particuler index ke chracter ko print krta hai
# print(str[3])#h
# print(str[2])#s

# #slice in string
# str="COMPUTER"
# print(str[2:4])


#adding the two string
# str1=input("enter your first name:")
# str2=input("enter your last name:")
# str=str1+" "+str2
# print("your name is:",str)



# str=input("enter your name:")
# print(len(str)) 
# # len is string function which is use for print the length of string


# # startwith()
# str="YASH"
# print(str.startswith("YA")) 
# # o/p-true
# print(str.startswith("SH"))
# # o/p-false

# endswith()

# str="yash"
# print(str.endswith("ya")) 
# # o/p-false
# print(str.endswith("sh"))
# # o/p-true

# # capitalize()

# str="yash jaiswal"
# print(str.capitalize())
# # o/p-Yash jaiswal  string ka first letter capital me ho jayega

# # replace()
# str="this is ram"
# print(str.replace(str,"python is more easy language"))
# #o/p-python

# find()

# str="this is my class"
# print(str.find("my"))
# # o/p-8 
# this method is print  or find the index value of string (including space count)


# #title
# str="aman tiwari"
# print(str.title())
# #o/p-Aman Tiwari


#wrong hai ye method run krne pr output error
# #swapcase
# str="Yash KUmar Jaiswal"
# print(str.swap())
# #o/p-yASH kuMAR jAISWAL


# #upper
# str="aman tiwari"
# print(str.upper())
# #o/p-AMAN TIWARI

# #lower
# str="AMAN TIWARI"
# print(str.lower())
# #o/p-aman tiwari

# #cout
# str="anand"
# print(str.count("d"))
# #o/p-1
# #how many time repeat the charecter

# #split
# str="I am student"
# print(str.split(" "))

# #or
# str1="I # am # student"
# print(str1.split("#"))

# #reverce
# # this method to print reverce of  string

# str="ARUN"
# print(str[::-1])
# #o/p-NURA

a=input("enter any string:")
b=list(a)
print(b)
c=(b.sort)
print(c.count())
