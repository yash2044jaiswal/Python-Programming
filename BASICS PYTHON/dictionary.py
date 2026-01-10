#  # dictionary in python syntax
# #example:
dict={
    #"key":value
    "name":"yash",                                     
    "cgpa":9.6,
    "marks":[98,89,78],
}
print(dict["name"])

# # onther exampele

# dict={
#     "name":"yash jaiswal",
#     "cgpa":9.8,
#     "marks":[89,97,76],
# }
# print(dict["name"],dict["cgpa"],dict["marks"])
# #we can add new in dictionary
# dict["id"]=158
# print(dict["name"],dict["cgpa"],dict["marks"],dict["id"])


# # try this
# info={
#     "key":"value",
#     "name":"yash jaiswal",
#     "learning":"python",
#     "age":19,
#     "is_adult":"true",
#     "marks":98.9,
#     "subject":["python","java","c++"],
#     "topics":("dict","set")
# }
# print(info)



# dict1={
#     "name":"yash jaiswal",
#     "age":19.8,
#     "marks":[89,97,76],
# }
# print(dict1["name"])
# print(dict1["age"])
# print(dict1["marks"])




# #nested dictionary
# student={
#     "name":"yash",
#     "score":{
#         "chem":89,
#         "phy":98,
#         "math":78
#     }
# }
# print(student)




# #dictionary method
# # dict.keys():it returns all key value in dictionary
# dict1={
#     "name":"yash jaiswal",
#     "age":19.8,
#     "marks":[89,97,76],
# }
# print(dict1.keys())
# #dict.value():it returns all values in dictionary
# print(dict1.values())
# #dict.items():it returns all (key,value)pairs as tupples
# print(dict1.items())
# #dict.get("keyname"):it return the key according to value
# print(dict1.get("name")) 
# #o/p-yash jaiswal

# #dict.update(newdict):it is used for insert the specified item to the dictionary
# dict1.update({"cgpa":9.8})
# print(dict1)

# #we can print the length of dictionry
# print(len(list(dict1.keys())))
# #or
# print(len(dict1))

#practice question
#wap to store following word meaning in dictionary
#table:"a picce of furniture","list of fact & figure"
#cat:"a small animal"

# word_dict={
#     "tabel":"a pice of furniture",
#     "cat":"a small animal"
# }
# print(word_dict.get(input("enter the key:")))



# wap to enter marks of 3 subject from the user and store them in a dictionary. start with an empty dictionary & add one by one .use subject name as key and marks as value.


# student={

# }
# print(student)
# student.update({input("enter the 1st subject name:"):input("enter the marks of subjet:")})
# print(student)
# student.update({input("enter the 2nd subject name:"):input("enter the marks of subjet:")})
# print(student)
# student.update({input("enter the 3rd subject name:"):input("enter the marks of subjet:")})
# print(student)

