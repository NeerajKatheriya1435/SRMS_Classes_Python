
# class Student:
#     name="Aman"
#     age=34

#     def showData(self):
#         print(f"My name is: {self.name} and age is: {self.age}")

# obj1=Student()
# obj2=Student()
# # print(obj1.name)
# # print(obj1.age)

# obj2.name="Krishna"
# obj2.age=42
# # print(obj2.name)
# # print(obj2.age)
# obj1.showData()
# obj2.showData()

# class Circle:
#     radius=7

#     def area(self):
#         var1=3.14*self.radius*self.radius
#         print("The area of circle is: ",(var1))

# c1=Circle()
# c1.area()

# c2=Circle()
# c2.radius=56
# c2.area()\

# Company1

# 5 Employee

# name1="Aman"
# age1=46
# salary1=3000

# name2="Sandeep"
# age2=48
# salary2=4000

# name3="Diva"
# age3=90
# salary3=8000

# print(f"My name is :{name1} and age: {age1} salary: {salary1}")
# print(f"My name is :{name2} and age: {age2} salary: {salary2}")
# print(f"My name is :{name3} and age: {age3} salary: {salary3}")

# class Employee:
#     name=""
#     age=0
#     salary=0

#     def showdata(self):
#         print(f"My name is :{self.name} and age: {self.age} salary: {self.salary}")

# emp1=Employee()

# emp1.name="John"
# emp1.age=67
# emp1.salary=2000

# emp2=Employee()
# emp2.name="Suman"
# emp2.salary=67000
# emp1.showdata()
# emp2.showdata()

# class Student:
#     def __init__(self,n1,a1):
#         self.name=n1
#         self.age=a1
#         print("Constructor called")
#     def show(self):
#         print("My name is: ",self.name)
#         print("My age is: ",self.age)

# s1=Student("Aman",45)
# s1.name="Shivam"
# print(s1.name)
# s2=Student("Diva",25)
# s1.show()
# s2.show()

# class Student:

#     def __init__(self,n1,a1):
#         self.name=n1
#     def show(self):
#         print("My name is: ",self.name)
    
#     @property
#     def getName(self):
#         return self.name
    
#     @getName.setter
#     def setName(self,name1):
#         self.name=name1

# s1=Student("Peter",56)
# s1.setName="Aman"
# print(s1.getName)
# s1.name="Suman"
# print(s1.name)

# s1.setName("Krishna")
# print(s1.getName())

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         print(f"My name is: {self.name}")
#         print(f"My salary is: {self.salary}")

# obj1=Employee("Shubham",34000)
# obj1.show()

# class Base:

#     def info(self):
#         print("I am a base class")
# # b1=Base()
# # b1.info()

# class Derived(Base):
#     def printDetails(self):
#         print("I am Derived Class")

# d1=Derived()

# d1.info()
# # d1.printDetails()
# class Aninmal:
#     def info(self):
#         print("I am a Animal")
# class Dog(Aninmal):
#     def printDetails(self):
#         print("I am Dog Class")
# class Random1(Dog):
#     def showData(self):
#         print("I am Third Class")
# d1=Dog()

# d1=Random1()
# d1.info()
# d1.printDetails()
# d1.showData()

# class A:
#     def show1(self):
#         print("This is my class A")
# class B:
#     def show2(self):
#         print("This is my class B")

# class C(A,B):
#     def data(self):
#         print("I am C class With Mutiple A,B")

# c1=C()
# c1.data()
# c1.show1()
# c1.show2()

# class A:
#     def __init__(self,name):
#         self.name=name
#         print("I am A Class")
#     # def show(self):
#     #     print("This is my class A")
# class B(A):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#         print("I am class B construtor",self.age)
#     # def show(self):
#     #     super().show()
#     #     print("This is my class B")

# b1=B()
# # b1.show()

# class Employee:
#     def __init__(self,name):
#         self.name=name
#         print("I am A Class")
# class Rahul(Employee):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#         print("I am class B construtor",self.age)
    
#     def showdata(self):
#         print("my name is: ",self.name)
#         print("my age is: ",self.age)

# b1=Rahul("Rahul",34)
# b1.showdata()
# b1.show()

# class Employee:
#     company="SRMS"
#     def __init__(self,name):
#         self.name=name

# emp1=Employee("Rahul")

# emp1.company="TechVision"
# Employee.company="TechVision"
# print(emp1.company)

# emp2=Employee("Aman")
# print(emp2.company)
# print(emp1.name)

class Employee:
    def __init__(self,p1,p2,p3):
        self.name=p1 # Public
        self._age=p2 # Protected
        self.__salary=p3

emp1=Employee("Rahul",23,10000)
print(emp1.name)
print(emp1._age)
print(emp1._Employee__salary)