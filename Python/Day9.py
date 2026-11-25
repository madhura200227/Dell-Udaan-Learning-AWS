""" DIFFERENCE BETWEEN RETURN AND PRINT"""
# def add(a, b):
#     print(a + b)
# x = add(2, 3)
# print(x) 

# def add(a, b):
#     print(a + b)
#     result = a + b
#     return result
# x = add(2, 3)
# print(x)

# def product(a, b):
#     print(a * b)
# x = product(2, 4)
# print(x)

# def product(a, b):
#     print(a * b)
#     result = a * b
#     return result
# x = product(2, 4)
# print(x)

# def product(a, b):
#     result = a * b
#     return result
# x = product(2, 4)
# print(x + 10)

# ### RECURSIVE FUNCTION
# def countdown(n):
#     if n == 0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n - 1)
# countdown(3)
"""output : 
3
2
1
Done
"""
# ### FACTORIAL OF A NUMBER
# def factorial(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

### LOCAL VARIABLES
"""LOCAL VARIABLES ARE DECLARED INSIDE THE FUNCTION AND CAN BE ACCESSED ONLY INSIDE THE FUNCTION"""
# def show_marks():
#     marks = 90 #LOCAL VARIABLE
#     print(marks)
# show_marks()

### GLOBAL VARIABLES
"""GLOBAL VARIABLES ARE DECLARED OUTSIDE THE FUNCTION AND CAN BE ACCESSED ANYWHERE IN THE PROGRAM"""
# course = "AWS" #GLOBAL VARIABLE
# def show_course():
#     print(course)
# show_course()
# print(course)

# count = 10 #GLOBAL VARIABLE
# def update_count():
#     count = 5 # LOCAL VARIABLE
#     print(count) 
# update_count()
# print(count)

# x = 10 #GLOBAL VARIABLE
# def test():
#      x = 20
#     print(x)
# test()
# print(x)

# x = 100
# def test1():
#     x = x + 10
#     print(x)
# test1()

# x = 1
# def func():
#     global x
"""global here is updating the value of x from 1 to 5"""
#     x = 2
#     x = x + 3
#     print(x)
# func()  
# print(x)

# def test2():
#     print("Hello")
#     return 10
#     """ after return statement the function will terminate and the below print statement will not be executed"""
#     print("Python")
# x = test2()
# print(x)

# def calculate(x):
#     x = x + 5
#     print(x)
#     return x * 2
# a = calculate(10)
# print(a)
# print(calculate(a))

### LAMBDA FUNCTION
"""A lambda function is a small anonymous function."""
# square = lambda x: x * x
# print(square(5))

# addition = lambda a, b: a + b
# print(addition(2, 4))

# product = lambda a , b: a * b
# print(product(2, 2))

# triple = 3
# product = lambda a, triple : a * triple
# print(product(4, triple))

# triple = lambda number : number * 3
# print(triple(4))

# Q1. 
"""Write a Python function to calculate the discounted price of an item after applying a discount percentage. 
The function should take two parameters: the original price and the discount percentage, 
and return the final price after the discount."""
# def discounted_price(price, discount_percentage):
#     discount_amount = price * discount_percentage / 100
#     return price - discount_amount
# print(discounted_price(200, 10))

### FILE 
""" open("filename", "mode") """
"""A file is a named location on disk to store related information.
Files are used to permanently store data in a non-volatile memory (e.g. hard disk)"""
# name = input("Enter the student name: ")
# print(name)
"""filename is the name of the file and mode is the way in which the file will be opened"""
# file = open("student.txt", "w")
# file.write("MADHURA")
# file.close
# name = input("Enter the student name: ")
# print(name)
# file = open("student.txt", "r")
# file.read("MADHURA")
# file.close

# name = input("Enter the student name: ")
# print(name)
# file = open("student.txt", "w")
# file.write("student name: Rakesh\n")
# file.write("student name: Madhura\n")
# file.write("student name: Ramesh\n")
# file.close

# students = ["Shivam", "Sachin", "Vidit"]
# file = open("student.txt", "w")
# for name in students:
#     file.write(name + "\n")
# file.close

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close

# students = ["Shivam", "Sachin", "Vidit"]
# file = open("student.txt", "w")
# count = file.write("Rahul")
# print(count)
# file.close

""" TO READ ONLY 2 LETTERS FROM THE FILE """
# file = open("student.txt", "r")
# data = file.read(2)
# print(data)
# file.close

### READLINE
"""reads single line"""
""" To read first line and second line in file"""
# file = open("student.txt", "r")
# first_line = file.readline()
# second_line = file.readline()
# print(first_line)
# print(second_line)
# file.close()

### READLINES
"""reads all lines from the file"""
# file = open("student.txt", "r")
# line = file.readlines()
# print("line : " ,line)
# file.close()

### FILE APPEND
""" append overwrites the data """
# file = open("student.txt", "a")
# data = file.write("Madhura \n")
# print(data)
# file.close()

# file = open("student.txt", "r+")
# data = file.read()
# print(data)
# file.write("\n Hello World")
# file.close()

# with open("student.txt", "r") as file:
#     data = file.read()
#     print(data)

# try : 
#     result = 10 / 1
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Successfull")
# finally:
#     print("Closing File")
