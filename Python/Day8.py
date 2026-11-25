# Q1.
# marks = int(input("Enter the marks of students: "))
# if 85 <= marks <= 100:
#     print("Grade A")
# elif 70 <= marks <= 84:
#     print("Grade B")
# elif 50 <= marks <= 69:
#     print("Grade C")
# elif 35 <= marks <= 49:
#     print("Pass")
# else:
#     print("Fail")

# Q2.

# marks = [45, 82, 37, 60, 29, 74, 90]
# passed_count = 0
# passed_total = 0
# for mark in marks:
#     if mark >= 40:
#         passed_count += 1
#         passed_total += 1
#         print("The Passed Students are: ",mark)
#     else:
#         print("The Student is failed")
# print("Students Passed: ", passed_count)
# print("Total Passing Marks: ", passed_total)

# Q3.

# correct_password = "python123"
# attempts = 0
# success = False
# while attempts < 3:
#     password = input("Enter the password: ")
#     attempts += 1
#     if password == correct_password:
#         success = True
#         print("Login Successful")
#         break
# if not success:
#     print("Account Locked")

### FUNCTION
""" FUNCTION IS A REUSABLE BLOCK OF CODE"""

"""SYNTAX OF FUNCTION"""
# def function_name(parameters):
#     #function body
#     return result
# function_name(arguments)

# def greet(): #declared function
#     print("WELCOME TO THE AWS ") #function body
# greet() #fucntion call

# def madhura():
#     print("Heyyy!! My Name is Madhuraa")
# madhura()
# madhura()

### FUNCTION PARAMETERS
"""PARAMETERS ARE USED IN FUNCTION BODY FOR WORKING ON THE OPERATIONS"""
# def calculate_total(a, b, c):
#     return a + b + c
# print("Calculate Total: ", calculate_total(10, 20, 30))
# print("Calculate Total: ", calculate_total(50, 95, 99))

"""Square of a Number"""
# def square(number):
#     result = number * number
#     # result = number ** 2
#     return result
# print("Square of two numbers are: ",square(2))

"""addition of two numbers"""
# def add(a, b):
#     result = a + b
#     return result
# print("the addition of two numbers are: ",add(10, 20))

# def introduce(name, age):
#     print("my name is : ", name)
#     print("my age is : ", age)
# introduce("Madhura", 20)

"""POSITIONAL ARGUMENTS"""
""" IF VALUE REVERSED THE OUPTUT WILL CHANGE"""
# def subtract(a, b):
#     print(a - b)
# subtract(10, 3)

"""KEYWORDS ARGUMENTS"""
""" KEYS ARE DEFINED FOLLOWED BY VALUES SO OUTPUT POSITION WILL NOT CHANGE"""
# def student(name, course):
#     print(name, course)
# student(course = "AWS CLOUD", name = "Madhura")

### DEFAULT ARGUMENTS
""" here course parameter is pre-defined"""
# def welcome(name, course = "AWS CLOUD"):
    # print(name, "is learning", course)
"""Rohan is learning AWS CLOUD"""
# welcome("Rohan") 
""" course = python becuase we overwrite the course"""
# welcome("Rohan", "Python")

# def add(a, b):
    # result = (a + b)
    # return result
# print("addition: ", add(6, 5))
# print("addition: ", add(9, 2, 1)) #TypeError: add() takes 2 positional arguments but 3 were given

### VARIABLE LENGTH ARGUMENTS
""" * single aestric means tuple"""
# def by_groceries(*items):
#     for item in items:
#         print("ITEM : ", item)
# by_groceries("apple", "mango", "tomato")

# def calculate_marks(*marks):
#     for mark in marks:
#         print("Marks entered: ", mark)
#         print(type(marks))
#         print("sum of marks: ", sum(marks))
# calculate_marks(99, 98, 92)

""" ** double aestric dictionary"""
# def show_profile(**info):
#     for key, value in info.items():
#         print(f"{key} : {value}")
# show_profile(name = "madhura", age = 20, city = "Pune")

# def add(a, b):
#     print(a + b)
#     result = a + b
#     # return result
# ans = add(2, 2)
# print("Addition : ", ans)

# def calculate(item, price):
#     result = item * price
#     result -= 100
#     return result
# total_bill = calculate(100, 2)
# print("total_bill: ", total_bill)

# def total_marks(marks):
#     if marks >= 45:
#         print("PASS")
#     else:
#         print("Failed")
# ans = total_marks(40)
# print(ans)

# marks = int(input("Enter the marks : "))
