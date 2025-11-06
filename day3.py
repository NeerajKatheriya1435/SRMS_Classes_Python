# list1=[4,9,6,1]
# list1[2]=80
# list1.append(77)
# list1.sort()
# list1.reverse()

# print(list1)

# tup1=(4,6,7)
# tup1[1]=99
# list2=list(tup1)
# list2.append(66)
# tup1=tuple(list2)
# print(tup1)
# print(type(tup1))

# tup2=(9,)
# print(type(tup2))


# dict1["name"]="John"
# print(dict1)
# print(dict1["age"])
# for item,value in dict1.items():
#     print(f"The value at {item} is: {value}")
# dict1={"name":"Ayush","age":34}
# inp1=input("Enter your key")

# for item in dict1:
#     if(item==inp1):
#         print("Key is Found")
#         break

# set1={5,7,3}
# set2={7,3,8}

# set2=set()
# print(type(set2))

# print(set1)

# age = int(input("Enter your age:"))
# try:
#     if age < 0:
#         raise ValueError("Age cannot be negative")

# except ValueError as e:
#     print("Excestion Error:",e)

# print("This My important line")
# age=15
# if(age>18):
#     print("Drive")
# else:
#     print("Not drive")

# status="Drive" if age>18 else "Not drive"
# print(status)

# x=67
# def greet():
#     # global x
#     x=56
#     print("Good Morning",x)

# # x=45
# greet()
# print(x)

# def squareFunc(val1):
#     print(val1*val1)

# squareFunc(4)
# lst=[4,7,2,3,9,6]
# square=lambda a:a+1
# print(square(3))
# lesthan5=lambda a:a<5

# list1=list(map(square,lst))
# list1=list(filter(lesthan5,lst))
# print(list1)

# def decorator(func1):
#     def wrapper():
#         print("Hello")
#         func1()
#         print("Bye Bye")
#     return wrapper

# @decorator
# def greet():
#     # print("Krishna")
#     print("AMAN")

# greet()

# import math
# print(math.sqrt(25))
# print(math.pow(75,2))

# from math import pow as p

# print(p(4,3))

# import os

# 1. os.getcwd()  => Get Current Working Directory
# print(os.getcwd())

# if not os.path.exists("AMAN"):
#     os.mkdir("AMAN")
#     print("File Created")

# else:
#     print("Already Created")

# import os

# for i in range(10):
    # os.mkdir(f"Rahul {i}")
    # os.rmdir(f"Rahul Kumar {i}")

# f1=open("rahul.txt","w")
# f1.write("Hello world I am good boy")
# f1.close()

# f = open("rahul.txt", "r")

# content= f.read()
# print(content)
# f.close()

# with open('rahul.txt', 'r') as f:
#   content=f.read()
    # content=f.readline()
    # f.seek(5)
    # content=f.readline()
    # print(f.tell())
    # print(content)

# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)

num1=int(input("Enter the number:"))
num2=num1
reverseNum=0
while(num1>0):
    lastDigit=num1%10
    reverseNum=reverseNum*10+lastDigit
    num1=num1//10

# print(reverseNum)
if(num2==reverseNum):
    print("Palindrome")
else:
    print("Not A palindrome")
