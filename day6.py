# 1. Write a program to print all even numbers from 1 to 50.

# for i in range(1,51):
#     if(i%2==0):
#         print(i,end=" ")

# 2. Write a program to find the largest of three numbers.

a=5
b=6
c=8

# if(a>b and a>c):
#     print("Gretest Number is: ",a)
# elif (b>a and b>c):
#     print("Gretest Number is: ",b)
# else:
#     print("Gretest Number is: ",c)

# 3. Write a program to check if a number is prime or not.

# num1=7

# for i in range(2,num1):
#     if(num1%i==0):
#         print("it is not prime number")
#         break

# 4. Write a program to count the digits in a number.

# count=0
# num1=int(input("Enter the number: "))
# while(num1>0):
#     count+=1
#     num1//=10
# print(count)
# 5. Write a program to reverse a number.

# num1=int(input("Enter the number: "))
# temp=num1
# rev=0
# while(num1>0):
#     lastdigit=num1%10
#     rev=rev*10+lastdigit
#     num1//=10
# # print(rev)
# if(temp==rev):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 6. Write a program to print multiplication table of a given number.

# inp1=int(input("Enter the number you want table: "))
# for i in range(1,11):
#     print(inp1,"X",i," = ",(inp1*i))

# 7. Write a program to find the sum of first N natural numbers.
# 8. Write a program to check if a character is a vowel or consonant.

# inp1=input("Enter the character: ")
# if inp1 in "aeiouAEIOU":
#     print("It is Vovel",inp1)
# else:
#     print("Consonants")
# 9. Write a program to find the highest and lowest number in a list.
# l1=[6,3,87,4,34,56]
# max=0
# for item in l1:
#     if(max<item):
#         max=item
# print(max)
# print(max(l1))
# print(min(l1))
# 10. Write a program to check if a string is a palindrome.

# str1="cac"
# # print(str1[::-1])
# if(str1==str1[::-1]):
#     print("String is Palindrome")
# else:
#     print("Not Palindrome")

# anagram
# str1="salt"
# str2="last45"
# if(sorted(str1)==sorted(str2)):
#     print("String is Anagram")
# else:
#     print("Not Anagram")
    

# 11. Write a program to count vowels in a string.
# 12. Write a program to find the second largest number in a list.
# 13. Write a program to remove duplicates from a list.
# 14. Write a program to find the sum of digits of a number.

# value=input("Enter the number: ")
# if (value!=""):
#     
# if (value:=input("Enter the value: "))!="":
#     print("Hello",value)

# line = input("Enter text (blank to stop): ")
# while line != "":
#     print("Line:", line)
#     line = input("Enter text (blank to stop): ")

# With Walrus
# while (line := input("Enter text (blank to stop): ")) != "":
#     print("Line:", line)

# l1=[i for i in range(40)]
# print(l1)

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# gen1=count_up_to(10)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# for item in gen1:
#     print(item)

# import random

# print("Your otp is: ",random.randint(1000,9999))

# fruits = ['apple', 'banana', 'mango', 'cherry']
# l1=[5,7,9,0]
# print(random.choice(fruits))
# random.shuffle(l1)
# print(l1)

# import time
# from functools import lru_cache

# @lru_cache(maxsize=None) 
# def square(n):
#     time.sleep(4)
#     print("I am stop")
#     return n*n

# print(square(6))
# print(square(6))
import re
# text = "My phone number is 123-566-7780"
# str1=re.search(r'\d{3}-\d{3}-\d{4}',text)
# print(str1.group())
# text="String may be long shubham456@gmail.com"
# str1=re.search(r'\w+@\w+\.\w+',text)
# print(str1.group())
import numpy as np
arr1=np.array([[6,5,3],[4,8,2],[3,8,3]])
print(arr1)
