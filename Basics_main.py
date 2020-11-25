# import cv2
# import math

# This is a comment  ---> Ctrl + /

'''
This is a multi-line comment
'''

# print(math.gcd(3,6))

# print("Hello World\n")

# print(5+8)

# a = 11 
# b = 'Harry' 
# c = 23.44 
# d = 2

# print(a+33)
# print(a+c)
# print(a/d)

# print(a**d)   #Exponentiation Operator --shows x to the power y
# print(a//d)   #Floor division operator --shows integer remainder
# print(a%d)    # Modulo Operator --shows ramainder

# typeA = type(a)
# typeB = type(b)
# print(typeB)

# e = "31"
# print(type(e))
# e = int(e)
# print(e)
# print(type(e))

# e = float(e)
# print(e)

# e = str(e)
# print(e)
# print(type(e))


# name = "Harry"
# print(name)
# print(name[0])
# print(name.strip())
# print(len(name))

# name = "Harry, Shubham, vikrant"
# var = name.lower()
# var = name.upper()
# var = name.replace("r", "t")
# var = name.replace(",", '\n')
# var = name.replace(", ", '\n')
# print(var)


# str1 = "This is a "
# str2 = "He is a "
# print(str1 + str2)

# name1 = "Harry"
# name2 = "Rohan"
# temp = "This is {1} and he is friends with {0}".format(name1, name2)
# temp = f"This is {name1} and works with {name2}"
# print(temp)


'''
Python Collections:
1. List
2. Tuple
3. Set
4. Dictionary
'''

#LIST
# lst = [61,2,3,5,6,41]
# var = type(lst)
# lst[2] = 45
# lst.append(100)
# lst.insert(1,11)
# lst.remove(61)
# lst.pop()
# del lst[3]
# del lst
# lst.clear()
# var = lst[1:4]
# var = len(lst)
# var = lst
# print(var)


# Tuple: items cannot be changed in a tuple
# a = ("Harry", "Shubh", "Rohan")
# var = a
# # a[0] = "Vikrant"  ----> cannot do this
# print(var)
# print(type(var))

# a = list(a)
# a[0] = "Vikrant"
# print(a)
# print(type(a))



# Set : no repetition is printed
# s1 = {2,3,3,4,4,5,5,2,2,4,2,4,3,3,6,1,8,9}
# s1.add(4444)
# s1.update([34,45,2,2,34,56,67,89])
# print(len(s1))
# s1.remove(1)
# s1.discard(1333) 
# Like list you can also use --->  .pop, .clear, .del
#and..intersection, union
# print(s1)


# Dictionary
# harryDict = {
#     "name": "Harry",
#     "marks": 34,
#     "city": "kota",
#     "country": "India"
# }
# print(harryDict)
# print(harryDict["marks"])
# harryDict["marks"] = 100
# print(harryDict)
# # del, clear, pop, update
# harryDict.pop("marks")
# print(harryDict)

# age = 18
# print(age)
# if(age>18):
#     print("you can drive")
# elif(age==18):
#     print("you are a teenager")
# else:
#     print("you cannot drive")



# Loops:
# for i in range(0,100):
#     print(i+1)

# li = [1, "abc", 4, 100, "hello"]
# for item in li:
#     print(item)


# Loops in sets and tuples
# s1 = {2,3,3,4,4,5,5,2,2,4,2,4,3,3,6,1,8,9}
# for i in s1:
#     print(i)

# a = ("Harry", "Shubh", "Rohan")
# for i in a:
#     print(i)

# Loops in Dictionary
harryDict = {
    "name": "Harry",
    "marks": 34,
    "city": "kota",
    "country": "India"
}
# for item in harryDict:
#     print(item)

# for item in harryDict.values():
#     print(item)
#OR
# for item in harryDict:
#     print(harryDict[item])

for x,y in harryDict.items():
    print(x,y)