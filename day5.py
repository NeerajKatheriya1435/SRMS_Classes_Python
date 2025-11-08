
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls, str1):
        name, age = str1.split('-')
        return cls(name, int(age))
    
    @staticmethod
    def multiPly(x,y,z):
        print(x*y*z)

    @staticmethod
    def factNum(num1):
        fact=1
        for i in range(1,num1+1):
            fact*=i
        print(fact)

    
str1="Ankit-56"
obj1=Student.from_string(str1)

# print(obj1.name)
# print(obj1.age)

# Student.multiPly(6,9,3)
# Student.factNum(3)
# print(obj1.__dict__)
# print(dir(Student))

# print(str(obj1))

# a=(6,8)
# b=(5,9)
# print(a+b)

# import time
# start1=time.time()
# for i in range(2000):
#     print(i)
# end1=time.time()

# start2=time.time()
# j=0
# while(j<2000):
#     print(j)
#     j=j+1
# end2=time.time()
# print(end1-start1)
# print(end2-start2)

import time
# local = time.localtime()
# print("Local time tuple:", local)
# print("Formatted:", time.strftime("%Y-%m-%d %H:%M:%S", local))
# Convert string to time

# time_str = "2025-07-16 11:00:00"
# parsed = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
# print("Parsed time tuple:", parsed)

# import asyncio
# async def task1():
#     print("Task 1 Started")
#     await asyncio.sleep(2)
#     print("Task 1 done")

# async def task2():
#     print("Task 2 Started")
#     await asyncio.sleep(2)
#     print("Task 2 done")

# async def main():
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())

from multiprocessing import Process

def calculate_square(numbers):
    print("Squares:")
    for n in numbers:
        print(f"{n}^2 = {n*n}")

def calculate_cube(numbers):
    print("Cubes:")
    for n in numbers:
        print(f"{n}^3 = {n*n*n}")

if __name__ == "__main__":
    nums = [2, 3, 4, 5]

    # Create processes
    p1 = Process(target=calculate_square, args=(nums,))
    p2 = Process(target=calculate_cube, args=(nums,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    print("Done with multiprocessing!")



