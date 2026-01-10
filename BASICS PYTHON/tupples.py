# #tuples syntax:
# tup=(2,1,3,4)
# print(type(tup))
# print(tup[0])
# print(tup[3])


# #empty tuple
# tup=()
# print(tup)
# print(type(tup))


# #syntax of single element of tuples

# tup=(1)
# print(tup)
# print(type(tup))#type int dega

# #corect sentance is:
# tup=(1,)
# print(tup)
# print(type(tup))
# #multiple elements ke liye last me (,) lagana jaruri nhi hai



# #slice method in tuple
# tup=(1,8,9,6,5)
# print(tup[1:3])
# #o/p- 8,9


# #index method in tuples
# tup=(2,3,4,5,6)
# print(tup.index(3))
# #o/p-1
# #jo value denge us value  ka index print krdega


#count method
#ye method ye bataata hai ki kisi element ki repeatation kitne bar hui hai
#syntx or ex
# tup=(1,2,3,4,52,2,42,2,2)
# print(tup.count(2))
#o/p-4
# #(kyo ki 2 tuple me 4 bar aaya hai)

#practice question
# #wap to count the number of student with the "A" grade in the folling tuple
# #("C","D","A","A","B","B","A")
# tup=("C","D","A","A","B","B","A")
# print(tup.count("A"))
# #store the above in a list & sort from "A" to "D"
# list1=(list(tup))
# print(list1)
# list1.sort()
# print(list1)


