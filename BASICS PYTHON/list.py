marks=[23,"yash",45,"harsh",89.9]
print(marks[1])#yash
print(marks[0])#23
print(marks[-3])#45
print(marks)#[23,"yash",45,"harsh",89.9]
print(len(marks))#5
print(marks[len(marks)-1])#89.9

# #sliceing in list
# #same as string
# marks=[23,"yash",45,"harsh",89.9]
# print(marks[1:3])#'yash',45
# print(marks[:4])#23,"yash",45,"harsh"
# print(marks[1:])
# print(marks[-3:-1])
# #reverse
# print(marks[::-1])


#list method

#append method(jodtaa hai)
# list=[4,7,5,54,44]
# list.append(89)
# print(list)
# #o/p- [4,7,5,54,44,89]


#sort method(sort in accending order)
# list=[67,89,90,34,47]
# list.sort()
# print(list)
# #34,47,67,89,90

# #sort(reverse=true) method -this method is for decending order
# li=[27,83,90,38,97]
# li.sort(reverse=True)
# print(li)
# #97,90,83,38,27

# #.reverse this method is print list in reversely
# list=[67,89,90,34,47]
# list.reverse()
# print(list)
# #47,34,90,89,67

# # insert - this method os insert the element at the particular index
# list=[67,89,90,34,47]
# list.insert(3,8)# list.insert(index,element)
# print(list)
# #67,89,90,8,34,47

# #remove method
# list=[56,67,8,76,6,90,6]
# list.remove(6)
# print(list)
# #56,67,8,76,90,6


# #pop method
# list=[67,89,90,34,47,90,89]#this method is remove the random value of the given list
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)


#practice question
#wap to ask user enter names of thier favraout movies & store them in list.
# list=[]
# a=input("enter first movie name:")
# b=input("enter second movie name:")
# c=input("enter third movie name:")

# list.append(a)
# list.append(b)
# list.append(c)
# print(list)

# #wap to check if a list contains a pallindrom of elements.(hint use copy()method)
# #(i)[1,2,3,2,1]
# list1=[1,2,3,2,1]
# # list2=[1,2,3]
# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("polindrom")
# else:
#     print("not pallindrom")    #polyndrom





# def print_full_name(first, last):
    
#     print(f"Hello {first} {last}! You just delved into python.")


# if __name__ == '__main__':
#     first_name = input("enter first name:")
#     last_name = input("enter second name:") 
#     print_full_name(first_name, last_name)  

  

# li=["hello",3,True,9.8,18]
# print(li[len(li)-1])
# for i in li:
#     print(i ,end=" ")



li=[1,0,0,2,'hi','',[]]
print(list(filter(bool,li)))